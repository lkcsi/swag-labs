from base.locators import CartPageLocators
from base.element import Item, BaseElement
from selenium.webdriver.common.by import By
from utilities import file_logger
import pages


class SortBy:
    AZ = "az"
    ZA = "za"
    LOHI = "lohi"
    HILO = "hilo"


class CartItem(Item):
    def __init__(self, driver, elem):
        super().__init__(elem)
        self.driver = driver

        data_test = elem.find_element(*CartPageLocators.REMOVE_BUTTON).get_attribute(
            "data-test"
        )
        self.remove_locator = (By.XPATH, f"//button[@data-test='{data_test}']")
        self.quantity = elem.find_element(*CartPageLocators.CART_QTY).text

    def __eq__(self, other):
        if isinstance(other, CartItem) and self.quantity == other.quantity:
            return True
        return super().__eq__(other)

    def click_remove(self):
        button = self.driver.find_element(*self.remove_locator)
        button.click()


class CheckoutButton(BaseElement):
    locator = CartPageLocators.CHECKOUT_BUTTON


class ContinueButton(BaseElement):
    locator = CartPageLocators.CONTINUE_BUTTON


class CartPage:
    logger = file_logger()
    TITLE = "Your Cart"
    checkout_button = CheckoutButton()
    continue_button = ContinueButton()

    def __init__(self, driver):
        self.driver = driver

    def continue_shopping(self):
        self.logger.info("click continue shopping button")
        self.continue_button.click()

    def checkout(self):
        self.logger.info("click checkout")
        self.checkout_button.click()
        return pages.CheckoutOnePage(self.driver)

    def get_items(self):
        driver = self.driver
        elements = driver.find_elements(*CartPageLocators.ITEM)
        return [CartItem(driver, elem) for elem in elements]
