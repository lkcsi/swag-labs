from pages.element import *
from selenium.common.exceptions import TimeoutException
from pages.locators import LoginPageLocators
from pages.locators import InventoryPageLocators
from pages.page import BasePage


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

    def click_submit(self):
        button = self.driver.find_element(*LoginPageLocators.SUBMIT)
        button.click()

    def _loaded(self):
        try:
            WebDriverWait(self.driver, 3).until(lambda d: d.find_element(*InventoryPageLocators.ITEM_LIST))
            return True
        except TimeoutException:
            return False

    def login(self, username, password):
        self.username_input = username
        self.password_input = password
        self.click_submit()
        return self._loaded()
