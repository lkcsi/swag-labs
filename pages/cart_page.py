import pages
from constants import CartPageLocators
from .elements import BaseElement, Item
from pages import BasePage
from selenium.webdriver.common.by import By
import logging
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as ec


class SortBy:
    AZ = "az"
    ZA = "za"
    LOHI = "lohi"
    HILO = "hilo"


class CartItem(Item):
    def __init__(self, container, driver, wait):
        super().__init__(container)
        self.driver = driver
        self.wait = wait

        data_test = container.find_element(*CartPageLocators.REMOVE_BUTTON).get_attribute("data-test")
        self.remove_locator = (By.XPATH, f"//button[@data-test='{data_test}']")
        self.quantity = container.find_element(*CartPageLocators.CART_QTY).text

    def __eq__(self, other):
        if isinstance(other, CartItem) and self.quantity == other.quantity:
            return True
        return super().__eq__(other)

    def click_remove(self):
        button = self.wait.until(ec.presence_of_element_located(self.remove_locator))
        button.click()


class CheckoutButton(BaseElement):
    locator = CartPageLocators.CHECKOUT_BUTTON


class ContinueButton(BaseElement):
    locator = CartPageLocators.CONTINUE_BUTTON


class CartPage(BasePage):
    TITLE = "Your Cart"
    checkout_button = CheckoutButton()
    continue_button = ContinueButton()

    def __init__(self, driver, wait):
        super().__init__(driver, wait)
        self.logger = logging.getLogger(CartPage.__name__)

    def continue_shopping(self):
        self.logger.info("click continue shopping button")
        self.continue_button.click()

    def checkout(self):
        self.logger.info("click checkout")
        self.checkout_button.click()
        return pages.CheckoutOnePage(self.driver, self.wait)

    def get_items(self):
        driver = self.driver
        wait = self.wait
        try:
            elements = wait.until(ec.presence_of_all_elements_located(CartPageLocators.ITEM))
        except TimeoutException:
            elements = []
        return [CartItem(elem, driver, wait) for elem in elements]
