# import unittest
# from parameterized.parameterized import parameterized_class
# from parameterized.parameterized import parameterized
# from database.database import users
# from base_test import BaseTestCase
# from pages.inventory_page import InventoryPage
# from pages.cart_page import CartPage
#
#
# @parameterized_class(users())
# class NavigationTestCase(BaseTestCase):
#     @parameterized.expand(
#         [("inventory", InventoryPage.TITLE), ("cart", CartPage.TITLE)]
#     )
#     def test_should_access_with_login(self, link, title):
#         self.login()
#         self.sauce_demo.get(f"{self.sauce_demo.PAGE_URL}/{link}.html")
#         self.assertEqual("", self.sauce_demo.login_page.error_text)
#         self.assertEqual(
#             title,
#             self.sauce_demo.get_title(),
#             f"Should navigate to {title} when logged in",
#         )
#
#     @parameterized.expand(
#         ["checkout-step-one", "checkout-step-two", "checkout-complete"]
#     )
#     def test_should_not_access_without_checkout(self, link):
#         self.login()
#         self.sauce_demo.get(f"{self.sauce_demo.PAGE_URL}/{link}.html")
#         self.assertEqual(
#             InventoryPage.TITLE,
#             self.sauce_demo.get_title(),
#             "Should stay in inventory page",
#         )
#
#
# class NavigationWithoutLogin(BaseTestCase):
#     @parameterized.expand(
#         [
#             "inventory",
#             "cart",
#             "checkout-step-one",
#             "checkout-step-two",
#             "checkout-complete",
#         ]
#     )
#     def test_should_not_access_without_login(self, link):
#         self.sauce_demo.get(f"{self.sauce_demo.PAGE_URL}/{link}.html")
#         error = self.sauce_demo.login_page.error_text
#         self.assertTrue(
#             f"You can only access '/{link}.html' when you are logged in." in error
#         )
#
#
# if __name__ == "__main__":
#     unittest.main()
