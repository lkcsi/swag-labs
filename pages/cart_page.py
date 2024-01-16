from pages.locators import CartPageLocators
from pages.element import Item, BaseElement, QuantityItem


class SortBy:
    AZ = "az"
    ZA = "za"
    LOHI = "lohi"
    HILO = "hilo"


class CartItem(Item):
    def __init__(self, driver, key):
        self.key = key
        self.driver = driver
        elem = driver.find_elements(*CartPageLocators.ITEM)[key]
        super().__init__(elem)
        self.quantity = elem.find_element(*CartPageLocators.CART_QTY).text

    def __eq__(self, other):
        if isinstance(other, CartItem) and self.quantity == other.quantity:
            return True
        return super().__eq__(other)

    def click_remove(self):
        elem = self.driver.find_elements(*CartPageLocators.ITEM)[self.key]
        button = elem.find_element(*CartPageLocators.REMOVE_BUTTON)
        button.click()


class CheckoutButton(BaseElement):
    locator = CartPageLocators.CHECKOUT_BUTTON


class CartPage:
    TITLE = "Your Cart"
    checkout_button = CheckoutButton()

    def __init__(self, driver):
        self.driver = driver

    def items(self):
        driver = self.driver
        size = len(driver.find_elements(*CartPageLocators.ITEM))
        return [CartItem(driver, i) for i in range(size)]
