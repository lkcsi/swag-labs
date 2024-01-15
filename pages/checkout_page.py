from pages.locators import CheckoutPageLocators
from pages.element import ValueElement, BaseElement, TextElement
from pages.page import BasePage


class FirstName(ValueElement):
    locator = CheckoutPageLocators.FIRST_NAME


class LastName(ValueElement):
    locator = CheckoutPageLocators.LAST_NAME


class PostalCode(ValueElement):
    locator = CheckoutPageLocators.POSTAL_CODE


class ContinueButton(BaseElement):
    locator = CheckoutPageLocators.CONTINUE


class CancelButton(BaseElement):
    locator = CheckoutPageLocators.CANCEL


class ErrorText(TextElement):
    locator = CheckoutPageLocators.ERROR


class CheckoutPage(BasePage):
    first_name = FirstName()
    last_name = LastName()
    postal_code = PostalCode()
    continue_button = ContinueButton()
    cancel_button = CancelButton()
    error_text = ErrorText()
