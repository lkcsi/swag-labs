from pages.locators import CompletePageLocators
from pages.element import BaseElement
from base.base_page import BasePage


class BackHomeButton(BaseElement):
    locator = CompletePageLocators.FINISH_BUTTON


class CompletePage(BasePage):
    TITLE = "Checkout: Complete!"
    back_home_button = BackHomeButton()
