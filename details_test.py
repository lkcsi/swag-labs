import unittest
from pages.inventory_page import InventoryItem
from parameterized import parameterized_class
from database.database import users
from base_test import BaseTestCase


@parameterized_class(users())
class InventoryTestCase(BaseTestCase):

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
