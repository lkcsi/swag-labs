from pages.locators import ItemLocators


class BaseElement(object):
    locator = ""


class ValueElement(BaseElement):
    def __set__(self, obj, value):
        driver = obj.driver
        element = driver.find_element(*self.locator)
        element.clear()
        element.send_keys(value)

    def __get__(self, obj, owner):
        driver = obj.driver
        element = driver.find_element(*self.locator)
        return element.get_attribute("value")


class TextElement(BaseElement):
    def __get__(self, obj, owner):
        driver = obj.driver
        element = driver.find_element(*self.locator)
        return element.text


class ListElement(BaseElement):
    def __get__(self, obj, owner):
        driver = obj.driver
        return driver.find_elements(*self.locator)


class Item(object):

    title_locator = ItemLocators.ITEM_TITLE
    desc_locator = ItemLocators.ITEM_DESC
    price_locator = ItemLocators.ITEM_PRICE

    def __init__(self, elem):
        self.elem = elem
        self.title = self.elem.find_element(*self.title_locator).text
        self.description = self.elem.find_element(*self.desc_locator).text
        price = self.elem.find_element(*self.price_locator).text
        self.price = float(price.replace("$", ""))

    def __eq__(self, other):
        if not isinstance(other, Item):
            return False
        return (
            self.title == other.title
            and self.description == other.description
            and self.price == other.price
        )


class ImageItem(Item):
    image_locator = ""

    def __init__(self, elem):
        self.elem = elem
        super().__init__(elem)
        image = self.elem.find_element(*self.image_locator)
        self.image = image.get_attribute("src").split("/")[-1]

    def __eq__(self, other):
        if isinstance(other, ImageItem) and self.image == other.image:
            return True
        return super().__eq__(other)
