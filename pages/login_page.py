from base import LoginPageLocators, BasePage, ValueElement, TextElement
import pages
from utilities import file_logger


class UsernameElement(ValueElement):
    locator = LoginPageLocators.USERNAME


class PasswordElement(ValueElement):
    locator = LoginPageLocators.PASSWORD


class LoginErrorElement(TextElement):
    locator = LoginPageLocators.ERROR


class LoginPage(BasePage):
    logger = file_logger()

    username_input = UsernameElement()
    password_input = PasswordElement()
    error_text = LoginErrorElement()

    def click_submit(self):
        self.logger.info("click submit button")
        button = self.driver.find_element(*LoginPageLocators.SUBMIT)
        button.click()

    def login(self, username, password):
        self.logger.info(f"type username: '{username}'")
        self.username_input = username
        self.logger.info(f"type password: '{password}'")
        self.password_input = password
        self.click_submit()
        return pages.InventoryPage(self.driver)
