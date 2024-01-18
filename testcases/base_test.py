# import unittest
# import logging
# from pages import (
#     InventoryPage,
#     CheckoutOnePage,
#     CheckoutTwoPage,
#     CompletePage,
#     CartPage,
# )
# from pages.element import Item
#
#
# class BaseTestCase(unittest.TestCase):
#     logger = logging.getLogger()
#     username = ""
#     password = ""
#     error = False
#
#     def setUp(self):
#         self.logger.setLevel(logging.INFO)
#         self.error = False
#
#     def login(self):
#         self.logger.info("user tries to login")
#         login_page = self.sauce_demo.login_page
#         login_page.login(self.username, self.password)
#         self.assertTrue(
#             self.sauce_demo.logged_in(),
#             f"Should be logged in error: {login_page.error_text}",
#         )
#
#     def logout(self):
#         self.logger.info("user tries to logout")
#         self.sauce_demo.burger.click()
#         self.sauce_demo.burger.click_logout()
#         self.assertFalse(self.sauce_demo.logged_in(), "Should be logged out")
#
#     def add_all_items(self):
#         inventory = self.sauce_demo.inventory_page
#         for item in inventory.get_items():
#             self.logger.info(f"add item :{item.title} to cart")
#             item.click_add()
#
#     def add_inventory_item(self, key):
#         inventory = self.sauce_demo.inventory_page
#         item = inventory.get_items()[key]
#         self.logger.info(f"add item :{item.title} to cart")
#         item.click_add()
#
#     def click_cart(self):
#         self.logger.info("click cart icon")
#         self.sauce_demo.cart.click()
#         self.__check_page(CartPage.TITLE)
#
#     def continue_shopping(self):
#         self.logger.info("click continue button")
#         self.sauce_demo.cart_page.continue_button.click()
#         self.__check_page(InventoryPage.TITLE)
#
#     def cancel_step_two(self):
#         self.logger.info("click cancel button")
#         self.sauce_demo.checkout_two_page.cancel_button.click()
#         self.__check_page(InventoryPage.TITLE)
#
#     def cancel_step_one(self):
#         self.logger.info("click cancel button")
#         self.sauce_demo.checkout_one_page.cancel_button.click()
#         self.__check_page(CartPage.TITLE)
#
#     def click_checkout(self):
#         self.logger.info("click checkout button")
#         self.sauce_demo.cart_page.checkout_button.click()
#         self.__check_page(CheckoutOnePage.TITLE)
#
#     def click_finish(self):
#         self.logger.info("click finish button")
#         self.sauce_demo.checkout_two_page.finish_button.click()
#         self.__check_page(CompletePage.TITLE)
#
#     def back_home(self):
#         self.logger.info("click back home button")
#         self.sauce_demo.complete_page.back_home_button.click()
#         self.__check_page(InventoryPage.TITLE)
#
#
#     def fill_billing_info(
#         self, first_name="standard", last_name="user", postal_code=8888
#     ):
#         self.logger.info("fill billing info")
#         self.sauce_demo.checkout_one_page.fill_info(first_name, last_name, postal_code)
#
#     def continue_to_step_two(self):
#         self.logger.info("click continue button")
#         checkout_one_page = self.sauce_demo.checkout_one_page
#         checkout_one_page.continue_button.click()
#         self.__check_page(CheckoutTwoPage.TITLE, checkout_one_page.error_text)
#
#     def compare_all_items(self, expected_items: list[Item], actual_items: list[Item]):
#         self.logger.info("compare expected items with actual items")
#         self.assertEqual(
#             len(expected_items), len(actual_items), "Item count should be the same"
#         )
#         self.assertListEqual(
#             expected_items, actual_items, "Items lists should be the same"
#         )
#
#     def compare(self, idx, expected_item: Item, actual_item: Item):
#         self.logger.info(
#             f"compare_{idx} expected_item: {expected_item} == actual_item: {actual_item}"
#         )
#         self.assertEqual(expected_item, actual_item)
#
#     def tearDown(self):
#         self.sauce_demo.close()
