from pages.locators import ItemLocators
from selenium.common.exceptions import NoSuchElementException


class BaseElement(object):
    locator = ""

    def __get__(self, obj, owner):
        driver = obj.driver
        return driver.find_element(*self.locator)


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
        try:
            element = driver.find_element(*self.locator)
            return element.text
        except NoSuchElementException:
            return ""


class Item(object):
    title_locator = ItemLocators.ITEM_TITLE
    desc_locator = ItemLocators.ITEM_DESC
    price_locator = ItemLocators.ITEM_PRICE

    def __str__(self):
        return (
            f"title: {self.title}, description: {self.description}, price: {self.price}"
        )

    def __init__(self, elem):
        self.title = elem.find_element(*self.title_locator).text
        self.description = elem.find_element(*self.desc_locator).text
        price = elem.find_element(*self.price_locator).text
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
        super().__init__(elem)
        image = elem.find_element(*self.image_locator)
        self.image = image.get_attribute("src").split("/")[-1]

    def __str__(self):
        return f"{super().__str__()}, image: {self.image}"

    def __eq__(self, other):
        if isinstance(other, ImageItem) and self.image == other.image:
            return True
        return super().__eq__(other)


class QuantityItem(Item):
    quantity_locator = ""

    def __init__(self, elem):
        super().__init__(elem)
        quantity = elem.find_element(*self.quantity_locator)
        self.quantity = int(quantity.text)

    def __str__(self):
        return f"{super().__str__()}, quantity: {self.quantity}"

    def __eq__(self, other):
        if isinstance(other, QuantityItem) and self.quantity == other.quantity:
            return True
        return super().__eq__(other)
