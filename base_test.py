import unittest
import logging
from pages.login_page import LoginPage
from pages.details_page import DetailsPage
from pages.inventory_page import InventoryPage
from pages.checkout_two_page import CheckoutTwoPage
from pages.complete_page import CompletePage
from pages.element import Item
from pages.checkout_one_page import CheckoutOnePage
from pages.cart_page import CartPage
from pages.header import Cart, SecondaryHeader, Burger
from selenium import webdriver


class BaseTestCase(unittest.TestCase):
    PAGE_URL = "https://www.saucedemo.com"
    logger = logging.getLogger()
    login_page = None
    inventory_page = None
    checkout_two_page = None
    cart_page = None
    checkout_one_page = None
    secondary_header = None
    details_page = None
    complete_page = None
    burger = None
    cart = None
    username = ""
    password = ""
    error = False

    def setUp(self):
        self.logger.setLevel(logging.INFO)
        self.driver = webdriver.Chrome()
        self.driver.get(self.PAGE_URL)
        self.login_page = LoginPage(self.driver)
        self.inventory_page = InventoryPage(self.driver)
        self.cart_page = CartPage(self.driver)
        self.checkout_one_page = CheckoutOnePage(self.driver)
        self.secondary_header = SecondaryHeader(self.driver)
        self.details_page = DetailsPage(self.driver)
        self.checkout_two_page = CheckoutTwoPage(self.driver)
        self.complete_page = CompletePage(self.driver)
        self.cart = Cart(self.driver)
        self.burger = Burger(self.driver)
        self.error = False
        self.driver.implicitly_wait(0.5)

    def login(self):
        self.logger.info("user tries to login")
        self.login_page.login(self.username, self.password)
        self.assertEqual(
            InventoryPage.TITLE,
            self.get_title(),
            f"Should proceed with valid credentials, error: {self.login_page.error_text}",
        )

    def logout(self):
        self.burger.click()
        self.burger.click_logout()
        self.assertTrue(self.login_page.button_displayed())

    def add_all_items(self):
        for item in self.inventory_page.get_items():
            self.logger.info(f"add item :{item.title} to cart")
            item.click_add()

    def add_inventory_item(self, key):
        self.inventory_page.get_items()[key].click_add()

    def click_cart(self):
        self.logger.info("click cart icon")
        self.cart.click()
        self.__check_page(CartPage.TITLE)

    def continue_shopping(self):
        self.logger.info("click continue button")
        self.cart_page.continue_button.click()
        self.__check_page(InventoryPage.TITLE)

    def cancel_step_two(self):
        self.logger.info("Click cancel button")
        self.checkout_two_page.cancel_button.click()
        self.__check_page(InventoryPage.TITLE)

    def cancel_step_one(self):
        self.logger.info("Click cancel button")
        self.checkout_one_page.cancel_button.click()
        self.__check_page(CartPage.TITLE)

    def click_checkout(self):
        self.logger.info("click checkout button")
        self.cart_page.checkout_button.click()
        self.__check_page(CheckoutOnePage.TITLE)

    def click_finish(self):
        self.logger.info("click finish button")
        self.checkout_two_page.finish_button.click()
        self.__check_page(CompletePage.TITLE)

    def back_home(self):
        self.logger.info("click back home button")
        self.complete_page.back_home_button.click()
        self.__check_page(InventoryPage.TITLE)

    def __check_page(self, expected_title):
        self.assertEqual(
            expected_title,
            self.get_title(),
            f"Should proceed to {expected_title}",
        )

    def get_title(self):
        return self.secondary_header.title()

    def fill_billing_info(
        self, first_name="standard", last_name="user", postal_code=8888
    ):
        self.logger.info("fill billing info")
        self.checkout_one_page.first_name = first_name
        self.checkout_one_page.last_name = last_name
        self.checkout_one_page.postal_code = postal_code

    def continue_to_step_two(self):
        self.checkout_one_page.continue_button.click()
        self.assertEqual(
            CheckoutTwoPage.TITLE,
            self.get_title(),
            f"Should proceed to {CheckoutTwoPage.TITLE}, error: {self.checkout_one_page.error_text}",
        )

    def compare_all_items(self, expected_items: list[Item], actual_items: list[Item]):
        self.assertEqual(len(expected_items), len(actual_items))
        self.assertListEqual(expected_items, actual_items)

    def compare(self, idx, expected_item: Item, actual_item: Item):
        self.logger.info(
            f"compare_{idx} expected_item: {expected_item} == actual_item: {actual_item}"
        )
        self.assertEqual(expected_item, actual_item)

    def tearDown(self):
        self.driver.close()
