from pages.locators import CartPageLocators
from pages.element import Item


class SortBy:
    AZ = "az"
    ZA = "za"
    LOHI = "lohi"
    HILO = "hilo"


class CartItem(Item):
    def __init__(self, elem):
        self.elem = elem
        super().__init__(elem)
        self.quantity = self.elem.find_element(*CartPageLocators.CART_QTY).text

    def __eq__(self, other):
        if isinstance(other, CartItem) and self.quantity == other.quantity:
            return True
        return super().__eq__(other)

    def click_remove(self):
        button = self.elem.find_element(*CartPageLocators.REMOVE_BUTTON)
        button.click()


class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.items = [CartItem(i) for i in driver.find_elements(*CartPageLocators.ITEM)]
