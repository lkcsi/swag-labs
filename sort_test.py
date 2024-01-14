import unittest
from parameterized import parameterized_class
from database.database import users
from pages.inventory_page import InventoryPage, SortBy
from base_test import BaseTestCase


@parameterized_class(users())
class SortTestCase(BaseTestCase):

    def test_order_az(self):
        self.order_by(SortBy.AZ, "title", lambda x: x["title"])

    def test_order_price_low_to_high(self):
        self.order_by(SortBy.LOHI, "price", SortTestCase.sort_by_price)

    def test_order_price_high_to_low(self):
        self.order_by(SortBy.HILO, "price", SortTestCase.sort_by_price, True)

    def test_order_za(self):
        self.order_by(SortBy.ZA, "title", lambda x: x["title"], True)

    def order_by(self, by: SortBy, key, sort_key, reverse=False):
        self.login()

        inventory_page = InventoryPage(self.driver)

        inventory_page.sort(by)

        items_in_order = [i.get_map() for i in inventory_page.items]
        items_in_order.sort(key=sort_key, reverse=reverse)

        for idx, item in enumerate(inventory_page.items):
            with self.subTest():
                self.compare(items_in_order[idx][key], item[key])

    def compare(self, item_1: str, item_2: str):
        self.logger.info(f"title expected: {item_1} == actual: {item_2}")
        self.assertEqual(item_1, item_2)

    @staticmethod
    def sort_by_price(item:dict):
        string = item['price'].replace("$", "")
        return float(string)


if __name__ == "__main__":
    unittest.main()
