import unittest
import logging
from pages.login_page import LoginPage
from pages.element import ImageItem
from pages.inventory_page import InventoryItem
from selenium import webdriver


class BaseTestCase(unittest.TestCase):
    logger = logging.getLogger()
    username = ""
    password = ""
    error = False

    def setUp(self):
        self.logger.setLevel(logging.INFO)
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.saucedemo.com")
        self.error = False

    def login(self):
        login_page = LoginPage(self.driver)
        if not login_page.login(self.username, self.password):
            self.fail("timeout")

    def compare(self, idx, item_1: InventoryItem, item_2: InventoryItem):
        self.logger.info(f"check item_{idx}")
        self.logger.info(f"{item_1.title} == {item_2.title}")
        self.logger.info(f"{item_1.description} == {item_2.description}")
        self.logger.info(f"{item_1.price} == {item_2.price}")
        if isinstance(item_1, ImageItem) and isinstance(item_2, ImageItem):
            self.logger.info(f"{item_1.image} == {item_2.image}")

        with self.subTest():
            self.assertEqual(item_1, item_2)

    def tearDown(self):
        self.driver.close()
