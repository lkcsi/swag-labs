import unittest
from pages.inventory_page import InventoryItem
from parameterized import parameterized_class
from database.database import users
from base_test import BaseTestCase


@parameterized_class(users())
class InventoryTestCase(BaseTestCase):
    expected = 0

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

    def __add(self, idx, item: InventoryItem):
        self.logger.info(f"click item_{idx} add to cart button")
        self.expected += 1
        item.click_add()

    def __remove(self, idx, item: InventoryItem):
        self.logger.info(f"click item_{idx} remove button")
        self.expected -= 1
        item.click_remove()

    def __check_counter(self):
        actual = self.cart.counter()
        self.logger.info(f"cart counter expected: {self.expected} == actual: {actual}")
        self.assertEqual(self.expected, actual)

    def test_open_with_image(self):
        self.__open_with(lambda x: x.click_title())

    def test_open_with_title(self):
        self.__open_with(lambda x: x.click_image())

    def __open_with(self, open_with_func):
        self.login()

        page_items = self.inventory_page.get_items()
        for idx, item in enumerate(page_items):
            open_with_func(item)
            details_item = self.details_page.item()
            self.compare(idx, item, details_item)
            self.driver.back()


if __name__ == "__main__":
    unittest.main()
