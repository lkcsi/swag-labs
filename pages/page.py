from .locators import *
from .element import *
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException
import logging

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

    def loaded(self):
        try:
            WebDriverWait(self.driver, 3).until(
                ec.presence_of_element_located(InventoryPageLocators.ITEM_LIST)
            )
            return True
        except TimeoutException:
            return False

    def login(self, username, password):
        self.username_input = username
        self.password_input = password
        self.click_submit()

class Item(object):
    def __init__(self, elem):
        self.elem = elem
    def title(self):
        return self.elem.find_element(*InventoryPageLocators.ITEM_TITLE).text

class Items():
    def __init__(self, driver):
        self.driver = driver

    def __getitem__(self, key):
        driver = self.driver
        items = driver.find_elements(*InventoryPageLocators.ITEM)
        return Item(items[key])

    def __len__(self):
        driver = self.driver
        items = driver.find_elements(*InventoryPageLocators.ITEM)
        return len(items)

class InventoryPage():
    def __init__(self, driver):
        self.driver = driver
        self.items = Items(driver)