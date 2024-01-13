from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException
from parameterized import parameterized_class
from selenium import webdriver
from database.database import users
import unittest

from pages.login_page import LoginPage
import pages.locators as locators


@parameterized_class(
    users()
)
class LoginTestCase(unittest.TestCase):
    username = ''
    password = ''

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.saucedemo.com")
        self.login_page = LoginPage(self.driver)

    def tearDown(self):
        self.driver.close()

    def test_happy_path(self):
        login_page = self.login_page
        driver = self.driver

        login_page.username_input = self.username
        login_page.password_input = self.password
        login_page.click_submit()

        try:
            WebDriverWait(driver, 3).until(
                expected_conditions.presence_of_element_located(locators.InventoryPageLocators.ITEM_LIST)
            )
            return
        except TimeoutException:
            self.fail(f'Unable to login, error: {login_page.error_text}')

    def test_wrong_password(self):
        login = self.login_page
        login.username_input = self.username
        login.password_input = 'invalid'
        login.click_submit()

        error = login.error_text
        if not error:
            self.fail("Login should fail with invalid credentials")

        assert 'Username and password do not match any user in this service' in error


class MissingParameters(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.saucedemo.com")
        self.login_page = LoginPage(self.driver)

    def tearDown(self):
        self.driver.close()

    def test_username_is_required(self):
        login = self.login_page
        login.password_input = "test"
        login.click_submit()
        assert 'Username is required' in login.error_text

    def test_password_is_required(self):
        login = self.login_page
        login.username_input = "test"
        login.click_submit()
        assert 'Password is required' in login.error_text


if __name__ == '__main__':
    unittest.main()
