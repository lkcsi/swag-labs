import database.database as database
from parameterized import parameterized_class
from selenium import webdriver
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.details_page import DetailsPage
from pages.header import Cart
import unittest
from base_test import BaseTestCase


@parameterized_class(database.users())
class CartTest(BaseTestCase, unittest.TestCase):
    def setUp(self):
        super(CartTest, self).setUp()
        self.expected = 0
        self.cart = Cart(self.driver)

    def test_inventory_cart_counter(self):
        self.login()
        inventory_page = InventoryPage(self.driver)

        self.assertEqual(0, self.cart.counter())

        for idx, item in enumerate(inventory_page.items):
            self.add(idx, item.click_add)

        for idx, item in enumerate(inventory_page.items):
            self.remove(idx, item.click_remove)

    def test_item_details_cart_counter(self):
        self.login()
        inventory_page = InventoryPage(self.driver)
        details_page = DetailsPage(self.driver)

        self.assertEqual(0, self.cart.counter())

        for idx, item in enumerate(inventory_page.items):
            item.click_image()

            self.add(idx, details_page.item.click_add)
            self.remove(idx, details_page.item.click_remove)

            self.driver.back()

    def add(self, idx, click):
        self.logger.info(f"click item_{idx} add to cart button")
        click()
        self.expected += 1
        self.check(self.cart.counter())

    def remove(self, idx, click):
        self.logger.info(f"click item_{idx} remove to cart button")
        click()
        self.expected -= 1
        self.check(self.cart.counter())

    def check(self, actual):
        self.logger.info(f"cart counter expected: {self.expected} == actual: {actual}")
        with self.subTest():
            self.assertEqual(self.expected, actual)


if __name__ == "__main__":
    unittest.main()
