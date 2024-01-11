from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import NoSuchElementException
from parameterized import parameterized
from selenium import webdriver
import unittest

class PyhonTestCase(unittest.TestCase):

    TIMEOUT = 5
    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.close()

    def get_element(self, by:By, type:str, value:str) -> WebElement :
        try:
            element = self.driver.find_element(by, f'//{type}[@id="{value}"]')
        except NoSuchElementException:
            element = None

        if not element:
            self.fail(f'Element <{type}> with id:{value} not found ')
        
        return element


    @parameterized.expand([
        ["standard_user", "secret_sauce"],
        ["locked_out_user", "secret_sauce"],
        ["problem_user", "secret_sauce"],
        ["performance_glitch_user", "secret_sauce"],
        ["error_user", "secret_sauce"],
        ["visual_error", "secret_sauce"],
    ])
    def test_case_1(self, username, password):
        driver = self.driver
        driver.get("https://www.saucedemo.com")

        username_input = driver.find_element(by=By.XPATH, value='//input[@id="user-name"]')
        password_input = driver.find_element(by=By.XPATH, value='//input[@id="password"]')
        submit_button = driver.find_element(by=By.XPATH, value='//input[@id="login-button"]')

        username_input.send_keys(username)
        password_input.send_keys(password)
        submit_button.click()
        
        try:
            _ = WebDriverWait(driver, self.TIMEOUT).until(
                expected_conditions.presence_of_element_located((By.ID, 'inventory_container'))
            )
        except:
            self.fail('inventory not shown after login')

if __name__ == '__main__':
    unittest.main()
