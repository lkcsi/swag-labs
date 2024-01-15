import unittest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.details_page import DetailsPage
import logging
from parameterized import parameterized_class
from database.database import users
from base_test import BaseTestCase


@parameterized_class(users())
class InventoryTestCase(BaseTestCase):
    # def test_inventory_items(self):
    #    self.login()
    #    inventory_page = self.inventory_page
    #    page_items = inventory_page.items
    #    db_items = database.items()
    #    assert len(page_items) == len(db_items)

    #    for idx, item in enumerate(page_items):
    #        self.compare('title', item.to_map(), db_items[idx])
    #        self.compare('image', item.to_map(), db_items[idx])
    #        self.compare('price', item.to_map(), db_items[idx])
    #        self.compare('description', item.to_map(), db_items[idx])

    #    if self.error:
    #        self.fail('Items are different than expected')

    def test_open_with_image(self):
        self.open_with(lambda x: x.click_title())

    def test_open_with_title(self):
        self.open_with(lambda x: x.click_image())

    def open_with(self, with_func):
        self.login()
        inventory_page = InventoryPage(self.driver)

        page_items = inventory_page.get_items()
        for idx, item in enumerate(page_items):
            with_func(item)
            details_page = DetailsPage(self.driver)

            details_item = details_page.item()
            self.compare(idx, item, details_item)

            self.driver.back()


if __name__ == "__main__":
    unittest.main()
