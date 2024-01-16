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

        self.compare_order(items_in_order, self.inventory_page.get_items(), by_func)

    def compare_order(self, expected_items: list[ImageItem], actual_items: list[ImageItem], by_func):

        expected_items = [by_func(i) for i in expected_items]
        actual_items = [by_func(i) for i in actual_items]

        self.logger.info(f"expected order: {expected_items} == actual: {actual_items}")
        self.assertEqual(expected_items, actual_items)


if __name__ == "__main__":
    unittest.main()
