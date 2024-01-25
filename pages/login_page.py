import logging

from pages.base_page import BasePage
from pages.inventory_page import InventoryPage
from constants.locators import LoginPageLocators, HeaderLocators
from .elements import ValueElement, TextElement
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException


class UsernameElement(ValueElement):
    locator = LoginPageLocators.USERNAME


class PasswordElement(ValueElement):
    locator = LoginPageLocators.PASSWORD


class LoginErrorElement(TextElement):
    locator = LoginPageLocators.ERROR


class LoginPage(BasePage):

    username_input = UsernameElement()
    password_input = PasswordElement()
    error_text = LoginErrorElement()

    def __init__(self, driver, wait):
        super().__init__(driver, wait)
        self.logger = logging.getLogger(LoginPage.__name__)

    def click_submit(self):
        self.logger.info("click submit button")
        button = self.wait.until(ec.presence_of_element_located(LoginPageLocators.SUBMIT))
        button.click()

    def login(self, username, password):
        self.logger.info(f"type username: '{username}'")
        self.username_input = username
        self.logger.info(f"type password: '{password}'")
        self.password_input = password
        self.click_submit()
        try:
            self.wait.until(ec.presence_of_element_located(HeaderLocators.TITLE))
        except TimeoutException:
            return None
        return InventoryPage(self.driver, self.wait)
