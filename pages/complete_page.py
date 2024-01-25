import logging
from constants.locators import CompletePageLocators
from .elements import BaseElement
from pages.base_page import BasePage


class BackHomeButton(BaseElement):
    locator = CompletePageLocators.FINISH_BUTTON


class CompletePage(BasePage):
    TITLE = "Checkout: Complete!"
    back_home_button = BackHomeButton()

    def __init__(self, driver, wait):
        super().__init__(driver, wait)
        self.logger = logging.getLogger(CompletePage.__name__)

    def back_to_home(self):
        self.logger.info("click back to home button")
        self.back_home_button.click()
