import database.database as database
from parameterized import parameterized_class
from pages.cart_page import CartPage
import unittest
from base_test import BaseTestCase


@parameterized_class(database.users())
class CartTest(BaseTestCase):
    def test_cart_content(self):
        self.login()

        items_to_buy = self.inventory_page.get_items()
        for item in items_to_buy:
            item.click_add()

        self.click_cart()

        self.assertEqual("Your Cart", self.get_title())

        items_in_cart = self.cart_page.items()
        self.assertEqual(len(items_to_buy), len(items_in_cart))

        for idx, item in enumerate(items_in_cart):
            item_to_buy = items_to_buy[idx]
            self.compare(idx, item_to_buy, item)

    def test_cart_remove(self):
        self.login()

        items_to_buy = self.inventory_page.get_items()
        for item in items_to_buy:
            item.click_add()

        self.click_cart()

        self.assertEqual("Your Cart", self.get_title())

        items_in_cart = self.cart_page.items()
        self.assertEqual(len(items_to_buy), len(items_in_cart))

        size = len(items_to_buy)
        for idx, item in enumerate(items_in_cart):
            self.logger.info(f"remove item_{idx} from cart")
            item.click_remove()
            size -= 1
            self.check_content_count(size)

    def check_content_count(self, expected):
        size = len(CartPage(self.driver).items())
        self.logger.info(f"cart items int list expected:{expected} == {size}")
        with self.subTest():
            self.assertEqual(expected, size)


if __name__ == "__main__":
    unittest.main()
