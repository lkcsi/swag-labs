from constants.locators import CheckoutPageOneLocators
from .elements import ValueElement, BaseElement, TextElement
from pages.base_page import BasePage
from pages.cart_page import CartPage
from pages.checkout_two_page import CheckoutTwoPage

import logging


class FirstName(ValueElement):
    locator = CheckoutPageOneLocators.FIRST_NAME


class LastName(ValueElement):
    locator = CheckoutPageOneLocators.LAST_NAME


class PostalCode(ValueElement):
    locator = CheckoutPageOneLocators.POSTAL_CODE


class ContinueButton(BaseElement):
    locator = CheckoutPageOneLocators.CONTINUE


class CancelButton(BaseElement):
    locator = CheckoutPageOneLocators.CANCEL


class ErrorText(TextElement):
    locator = CheckoutPageOneLocators.ERROR


class CheckoutOnePage(BasePage):
    TITLE = "Checkout: Your Information"

    first_name = FirstName()
    last_name = LastName()
    postal_code = PostalCode()
    continue_button = ContinueButton()
    cancel_button = CancelButton()
    error_text = ErrorText()

    def __init__(self, driver, wait):
        super().__init__(driver, wait)
        self.logger = logging.getLogger(CheckoutOnePage.__name__)

    def cancel(self):
        self.logger.info("click cancel checkout")
        self.cancel_button.click()

        return CartPage(self.driver, self.wait)

    def fill_info(self, first_name="John", last_name="McClain", postal_code=8888):
        self.logger.info(f"type First Name: {first_name}")
        self.first_name = first_name
        self.logger.info(f"type Last Name: {last_name}")
        self.last_name = last_name
        self.logger.info(f"type Postal Code: {postal_code}")
        self.postal_code = postal_code

    def fill_and_continue(self, first_name="John", last_name="McClain", postal_code=8888):
        self.fill_info(first_name, last_name, postal_code)
        self.logger.info(f"click continue button")
        self.continue_button.click()

        return CheckoutTwoPage(self.driver, self.wait)
