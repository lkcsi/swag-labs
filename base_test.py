import unittest
import logging
from pages.login_page import LoginPage
from pages.details_page import DetailsPage
from pages.element import ImageItem
from pages.inventory_page import InventoryPage
from pages.overview_page import OverviewPage
from pages.complete_page import CompletePage
from pages.element import Item
from pages.checkout_page import CheckoutPage
from pages.cart_page import CartPage
from pages.header import Cart, SecondaryHeader
from selenium import webdriver


class BaseTestCase(unittest.TestCase):
    logger = logging.getLogger()
    login_page = None
    inventory_page = None
    overview_page = None
    cart_page = None
    checkout_page = None
    secondary_header = None
    details_page = None
    complete_page = None
    cart = None
    username = ""
    password = ""
    error = False

    def setUp(self):
        self.logger.setLevel(logging.INFO)
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.saucedemo.com")
        self.login_page = LoginPage(self.driver)
        self.inventory_page = InventoryPage(self.driver)
        self.cart_page = CartPage(self.driver)
        self.checkout_page = CheckoutPage(self.driver)
        self.secondary_header = SecondaryHeader(self.driver)
        self.details_page = DetailsPage(self.driver)
        self.overview_page = OverviewPage(self.driver)
        self.complete_page = CompletePage(self.driver)
        self.cart = Cart(self.driver)
        self.error = False

    def login(self):
        login_page = self.login_page
        if not login_page.login(self.username, self.password):
            self.fail("timeout")

    def add_all_items(self):
        for item in self.inventory_page.get_items():
            item.click_add()

    def add_inventory_item(self, key):
        self.inventory_page.get_items()[key].click_add()

    def click_cart(self):
        self.cart.click()

    def click_checkout(self):
        self.cart_page.checkout_button.click()

    def get_title(self):
        return self.secondary_header.title()

    def fill_billing_info(self):
        self.checkout_page.first_name = "test_name"
        self.checkout_page.last_name = "test_name"
        self.checkout_page.postal_code = "8888"
        self.checkout_page.continue_button.click()

    def compare(self, idx, item_1: Item, item_2: Item):
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
