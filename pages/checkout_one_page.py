from pages.locators import CheckoutPageOneLocators
from pages.element import ValueElement, BaseElement, TextElement
from base.base_page import BasePage


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

    def fill_info(self, first_name, last_name, postal_code):
        self.first_name = first_name
        self.last_name = last_name
        self.postal_code = postal_code
