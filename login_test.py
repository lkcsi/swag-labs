from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from parameterized import parameterized
from selenium import webdriver
import unittest
import page, locators

class PyhonTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.saucedemo.com")

    def tearDown(self):
        self.driver.close()

    @parameterized.expand([
        ["standard_user", "secret_sauce"],
        ["locked_out_user", "secret_sauce"],
        ["problem_user", "secret_sauce"],
        ["performance_glitch_user", "secret_sauce"],
        ["error_user", "secret_sauce"],
        ["visual_user", "secret_sauce"],
    ])
    def test_happy_path(self, username, password):
        driver = self.driver

        login = page.LoginPage(driver)
        login.username_input = username
        login.password_input = password
        login.click_submit()

        try:
            WebDriverWait(driver, 3).until(
                expected_conditions.presence_of_element_located((By.ID, 'inventory_container'))
            )
            return
        except: 
            self.fail(f'Unable to login, error: {login.get_error()}')

    @parameterized.expand([
        ["standard_user", "secret_auce"],
        ["locked_out_user", "ecret_sauce"],
        ["problem_user", "secre_sauce"],
        ["performance_glitch_user", "scret_sauce"],
        ["error_user", "secret_sauc"],
        ["visual_user", "secretsauce"],
    ])
    def test_wrong_password(self, username, password):
        driver = self.driver

        login = page.LoginPage(driver)
        login.username_input = username
        login.password_input = password
        login.click_submit()

        error = login.get_error()
        if(not error):
            self.fail("Login should fail with invalid credentials")

        assert 'Username and password do not match any user in this service' in error

if __name__ == '__main__':
    unittest.main()
