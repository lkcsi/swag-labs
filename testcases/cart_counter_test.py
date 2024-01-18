# import database.database as database
# from parameterized import parameterized_class
# import unittest
# from base_test import BaseTestCase
#
#
# @parameterized_class(database.users())
# class CartTest(BaseTestCase, unittest.TestCase):
#     expected = 0
#
#     def test_cart_counter_from_details(self):
#         inventory_page = self.sauce_demo.inventory_page
#         details_page = self.sauce_demo.details_page
#         self.expected = 0
#         self.login()
#         self.__check_counter()
#
#         for item in inventory_page.get_items():
#             item.click_image()
#             self.__add(details_page.item())
#             self.__check_counter()
#             self.sauce_demo.back()
#
#         for item in inventory_page.get_items():
#             item.click_image()
#             self.__remove(details_page.item())
#             self.__check_counter()
#             self.sauce_demo.back()
#
#     def test_cart_counter_from_inventory(self):
#         inventory_page = self.sauce_demo.inventory_page
#         self.expected = 0
#         self.login()
#
#         self.__check_counter()
#
#         for item in inventory_page.get_items():
#             self.__add(item)
#             self.__check_counter()
#
#         for item in inventory_page.get_items():
#             self.__remove(item)
#             self.__check_counter()
#
#     def __add(self, item):
#         self.logger.info(f"click item's {item.title} add to cart button")
#         self.expected += 1
#         item.click_add()
#
#     def __remove(self, item):
#         self.logger.info(f"click item's {item.title} remove button")
#         self.expected -= 1
#         item.click_remove()
#
#     def __check_counter(self):
#         actual = self.sauce_demo.cart.counter()
#         self.logger.info(f"cart counter expected: {self.expected} == actual: {actual}")
#         self.assertEqual(self.expected, actual)
#
#
# if __name__ == "__main__":
#     unittest.main()
