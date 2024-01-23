import logging

from base import CompletePageLocators, BasePage, BaseElement
from utilities import file_logger


class BackHomeButton(BaseElement):
    locator = CompletePageLocators.FINISH_BUTTON


class CompletePage(BasePage):
    TITLE = "Checkout: Complete!"
    back_home_button = BackHomeButton()

    def __init__(self, driver):
        super().__init__(driver)
        self.logger = logging.getLogger(CompletePage.__name__)

    def back_to_home(self):
        self.logger.info("click back to home button")
        self.back_home_button.click()
