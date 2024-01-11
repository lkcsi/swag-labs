from selenium import webdriver
from locators import LoginPageLocators
import element

class BasePage(object): 
    def __init__(self, driver):
        self.driver = driver

class UsernameElement(element.TextElement):
    locator = LoginPageLocators.USERNAME

class PasswordElement(element.TextElement):
    locator = LoginPageLocators.PASSWORD

class LoginPage(BasePage):
    username_input = UsernameElement()
    password_input = PasswordElement()

    def click_submit(self):
        button = self.driver.find_element(*LoginPageLocators.SUBMIT)
        button.click()