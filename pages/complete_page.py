from pages.locators import CheckoutPageLocators, CompletePageLocators
from pages.element import ValueElement, BaseElement, TextElement
from pages.page import BasePage


class BackHomeButton(BaseElement):
    locator = CompletePageLocators.FINISH_BUTTON


class CompletePage(BasePage):
    TITLE = "Checkout: Complete!"
    back_home_button = BackHomeButton()
