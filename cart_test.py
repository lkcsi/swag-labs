import database.database as database
from parameterized import parameterized_class
from selenium import webdriver
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.details_page import DetailsPage
from pages.header import Cart
import unittest
import logging


@parameterized_class(
    database.users()
)
class MyTestCase(unittest.TestCase):
    logger = logging.getLogger()
    username = ''
    password = ''
    expected = 0
    success = True

    def setUp(self):
        self.logger.setLevel(logging.INFO)
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.saucedemo.com")

        self.login_page = LoginPage(self.driver)
        self.inventory_page = InventoryPage(self.driver)
        self.details_page = DetailsPage(self.driver)
        self.cart = Cart(self.driver)

    def login(self):
        login_page = self.login_page
        if not login_page.login(self.username, self.password):
            self.fail('timeout')

    def test_inventory_cart_counter(self):
        self.login()
        inventory_page = self.inventory_page

        assert self.cart.counter() is 0
        for idx, item in enumerate(inventory_page.items):
            item.click_add()
            self.add(idx, self.cart.counter())

        for idx, item in enumerate(inventory_page.items):
            item.click_add()
            self.remove(idx, self.cart.counter())

        self.assertTrue(self.success, "Counter should be match user interaction")

    def test_item_details_cart_counter(self):
        self.login()
        inventory_page = self.inventory_page
        details_page = self.details_page

        assert self.cart.counter() is 0
        for idx, item in enumerate(inventory_page.items):
            item.click_image()
            details_page.item.click_add()
            self.add(idx, self.cart.counter())
            details_page.item.click_add()
            self.remove(idx, self.cart.counter())
            self.driver.back()

        self.assertTrue(self.success, "Counter should be match user interaction")

    def add(self, idx, actual):
        self.logger.info(f'click item_{idx} add to cart button')
        self.expected += 1
        self.check(actual)

    def remove(self, idx, actual):
        self.logger.info(f'click item_{idx} remove to cart button')
        self.expected -= 1
        self.check(actual)

    def check(self, actual):
        self.logger.info(f'expected: {self.expected} == actual: {actual}')
        if not self.expected == actual:
            self.success = False

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
