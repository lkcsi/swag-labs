from PIL import Image, ImageDraw
import os
import uuid


def compare_images(img_1: str, img_2: str, file_name: str) -> bool:
    result = True
    img_correct = Image.open(f"screenshots/{img_1}.png")
    img_tested = Image.open(f"screenshots/{img_2}.png")
    columns, rows = 60, 80

    img_width, img_height = img_tested.size

    block_width = img_width // columns
    block_height = img_height // rows

    for y in range(0, img_height - block_height, block_height + 1):
        for x in range(0, img_width - block_width, block_width + 1):
            region_tested = __get_region(img_tested, x, y, block_width, block_height)
            region_correct = __get_region(img_correct, x, y, block_width, block_height)

            if region_tested is not None and region_correct is not None and region_correct != region_tested:
                draw = ImageDraw.Draw(img_tested)
                draw.rectangle((x, y, x + block_width, y + block_height), outline="red")
                result = False

    img_tested.save(f"screenshots/{file_name}.png")
    return result


def __get_region(image, x, y, width, height):
    region_total, factor = 0, 100

    for coord_y in range(y, y + height):
        for coord_x in range(x, x + width):
            pixel = image.getpixel((coord_x, coord_y))
            region_total += sum(pixel) / 4

    return region_total / factor


def save_image(item):
    driver = item.cls.driver
    file_path = os.path.join("screenshots", f"{str(uuid.uuid4())}.png")
    if result := visual_test(item):
        file_path = save_compare_result(result, file_path)
    else:
        driver.save_screenshot(file_path)
    return (f"<div><img src='../{file_path}' alt='screenshot' style='width:300px;height:200px'"
            "onclick='window.open(this.src)' align='right'/><div>")


def visual_test(item):
    for marker in item.own_markers:
        if marker.name == 'visualtest':
            return marker.args[0]


def save_compare_result(result, file_path):
    compare_result = f"screenshots/{result}.png"
    if os.path.exists(compare_result):
        os.rename(compare_result, file_path)
        return file_path
    return ""
