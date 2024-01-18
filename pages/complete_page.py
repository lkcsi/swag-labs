from base.locators import CompletePageLocators
from base.element import BaseElement
from base.base_page import BasePage
from utilities import file_logger


class BackHomeButton(BaseElement):
    locator = CompletePageLocators.FINISH_BUTTON


class CompletePage(BasePage):
    TITLE = "Checkout: Complete!"
    back_home_button = BackHomeButton()
    logger = file_logger()

    def back_to_home(self):
        self.logger.info("click back to home button")
        self.back_home_button.click()
