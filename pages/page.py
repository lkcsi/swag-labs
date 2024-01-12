from .locators import LoginPageLocators
from .element import ValueElement
from .element import TextElement

class BasePage(object): 
    def __init__(self, driver):
        self.driver = driver

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
