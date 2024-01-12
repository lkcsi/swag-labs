from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from parameterized import parameterized
from selenium import webdriver
import unittest
import pages.page as page
import pages.locators as locators
from params.param_loader import params_from_file

class LoginTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.saucedemo.com")
        self.login_page = page.LoginPage(self.driver)

    def tearDown(self):
        self.driver.close()

    @parameterized.expand(
           params_from_file('params/users.json')
    )
    def test_happy_path(self, username, password):
        login_page = self.login_page
        driver = self.driver

        login_page.username_input = username
        login_page.password_input = password
        login_page.click_submit()

        try:
            WebDriverWait(driver, 3).until(
                expected_conditions.presence_of_element_located(locators.InventoryPageLocators.ITEM_LIST)
            )
            return
        except: 
            self.fail(f'Unable to login, error: {login_page.error_text}')

    @parameterized.expand(
            params_from_file('params/invalid_passwords.json')
    )
    def test_wrong_password(self, username, password):
        login = self.login_page
        login.username_input = username
        login.password_input = password
        login.click_submit()

        error = login.error_text
        if(not error):
            self.fail("Login should fail with invalid credentials")

        assert 'Username and password do not match any user in this service' in error

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
