import unittest
from parameterized import parameterized_class
from database.database import users
from pages.inventory_page import InventoryPage, SortBy
from base_test import BaseTestCase
from pages.element import ImageItem


@parameterized_class(users())
class SortTestCase(BaseTestCase):
    def test_order_az(self):
        self.order_by(SortBy.AZ, lambda x: x.title)

    def test_order_price_low_to_high(self):
        self.order_by(SortBy.LOHI, lambda x: x.price)

    def test_order_price_high_to_low(self):
        self.order_by(SortBy.HILO, lambda x: x.price, True)

    def test_order_za(self):
        self.order_by(SortBy.ZA, lambda x: x.title, True)

    def order_by(self, by: SortBy, by_func, reverse=False):
        self.login()

        self.inventory_page.sort(by)

        items_in_order = self.inventory_page.get_items()
        items_in_order.sort(key=by_func, reverse=reverse)

        for idx, item in enumerate(self.inventory_page.get_items()):
            with self.subTest():
                self.compare_by(items_in_order[idx], item, by_func)

    def compare_by(self, item_1: ImageItem, item_2: ImageItem, by_func):
        self.logger.info(f"expected: {by_func(item_1)} == actual: {by_func(item_2)}")
        self.assertEqual(by_func(item_1), by_func(item_2))


if __name__ == "__main__":
    unittest.main()
