import database.database as database
from parameterized import parameterized_class
import unittest
from base_test import BaseTestCase


@parameterized_class(database.users())
class CartTest(BaseTestCase):
    def test_cart_content_from_inventory(self):
        self.login()
        inventory_items = self.inventory_page.get_items()
        items_to_buy = []
        for idx, item in enumerate(inventory_items):
            self.add_inventory_item(idx)
            items_to_buy.append(item)
            self.click_cart()
            self.compare_all_items(items_to_buy, self.cart_page.items())
            self.continue_shopping()

    def test_cart_content_from_details(self):
        self.login()
        inventory_items = self.inventory_page.get_items()
        items_to_buy = []
        for idx, item in enumerate(inventory_items):
            item.click_image()
            self.details_page.item().click_add()
            items_to_buy.append(item)
            self.click_cart()
            self.compare_all_items(items_to_buy, self.cart_page.items())
            self.continue_shopping()

    def test_cart_remove(self):
        self.login()
        items_to_buy = self.inventory_page.get_items()
        self.add_all_items()
        self.click_cart()
        items_in_cart = self.cart_page.items()

        self.compare_all_items(items_to_buy, items_in_cart)

        for idx, item in enumerate(items_in_cart):
            self.__remove(idx, item)
            items_to_buy.pop(0)
            self.compare_all_items(items_to_buy, self.cart_page.items())

    def __remove(self, idx, item):
        self.logger.info(f"remove item_{idx} from cart")
        item.click_remove()


if __name__ == "__main__":
    unittest.main()
