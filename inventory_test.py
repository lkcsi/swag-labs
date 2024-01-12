import unittest
from selenium import webdriver
import pages.page as page
import logging
import pytest, textcheck
from parameterized import parameterized
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from params.param_loader import params_from_file

class InventoryTestCase(unittest.TestCase):
    logger = logging.getLogger()
    def setUp(self):
        self.logger.setLevel(logging.INFO)
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.saucedemo.com")
        self.login_page = page.LoginPage(self.driver)
        self.inventory_page = page.InventoryPage(self.driver)
    
    @parameterized.expand(
           params_from_file('params/users.json')
    )
    def test_inventory_has_items(self, username, password):
        inventory_page = self.inventory_page

        self.login_page.login(username, password)
        if not self.login_page.loaded():
            self.fail('timeout')

        assert len(inventory_page.items) > 0

    @parameterized.expand(
           params_from_file('params/users.json')
    )
    def test_all_titles(self, username, password):
        inventory_page = self.inventory_page

        self.login_page.login(username, password)
        if not self.login_page.loaded():
            self.fail('timeout')

        titles = []
        for item in inventory_page.items:
            titles.append(item.title())
        
        errors = self.get_errors(titles)
        if self.get_errors():
            self.fail(errors)

    def get_errors(self, texts:[str]):
        errors = []
        for item in texts:
            res = textcheck.check(item)
            if res:
                errors.append(f'element has: {res}')


    def tearDown(self):
       self.driver.close()

if __name__ == '__main__':
    unittest.main()