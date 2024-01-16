import database.database as database
from parameterized import parameterized_class
import unittest
from base_test import BaseTestCase


@parameterized_class(database.users())
class CartTest(BaseTestCase, unittest.TestCase):
    expected = 0

    def test_cart_counter_from_details(self):
        self.expected = 0
        self.login()
        self.__check_counter()

        for idx, item in enumerate(self.inventory_page.get_items()):
            item.click_image()
            self.__add(idx, self.details_page.item().click_add)
            self.__check_counter()
            self.driver.back()

        for idx, item in enumerate(self.inventory_page.get_items()):
            item.click_image()
            self.__remove(idx, self.details_page.item().click_remove)
            self.__check_counter()
            self.driver.back()

    def test_cart_counter_from_inventory(self):
        self.expected = 0
        self.login()

        self.__check_counter()

        for idx, item in enumerate(self.inventory_page.get_items()):
            self.__add(idx, item.click_add)
            self.__check_counter()

        for idx, item in enumerate(self.inventory_page.get_items()):
            self.__remove(idx, item.click_remove)
            self.__check_counter()

    def __add(self, idx, add_func):
        self.logger.info(f"click item_{idx} add to cart button")
        self.expected += 1
        add_func()

    def __remove(self, idx, remove_func):
        self.logger.info(f"click item_{idx} remove button")
        self.expected -= 1
        remove_func()

    def __check_counter(self):
        actual = self.cart.counter()
        self.logger.info(f"cart counter expected: {self.expected} == actual: {actual}")
        self.assertEqual(self.expected, actual)


if __name__ == "__main__":
    unittest.main()
