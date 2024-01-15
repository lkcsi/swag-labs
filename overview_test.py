import unittest
from base_test import BaseTestCase


class OverViewTestCase(BaseTestCase):
    username = "standard_user"
    password = "secret_sauce"

    def test_complete(self):
        self.login()
        self.add_all_items()
        self.click_cart()
        self.click_checkout()
        self.fill_billing_info()
        self.overview_page.finish_button.click()

        self.assertEqual("Checkout: Complete!", self.get_title())

        self.complete_page.back_home_button.click()

        self.assertEqual("Products", self.get_title())

    def test_totals(self):
        self.login()
        self.add_all_items()

        items_to_buy = self.inventory_page.get_items()

        self.click_cart()
        self.click_checkout()
        self.fill_billing_info()

        subtotal = 0
        for item in items_to_buy:
            subtotal += item.price

        actual = self.overview_page.subtotal.replace("Item total: $", "")
        actual = float(actual)

        self.assertEqual(subtotal, actual)
        total = subtotal * tax

    def test_overview_items(self):
        self.login()
        self.add_all_items()

        items_to_buy = self.inventory_page.get_items()

        self.click_cart()
        self.click_checkout()
        self.fill_billing_info()

        overview_items = self.overview_page.get_items()

        self.assertEqual(len(items_to_buy), len(overview_items))
        for idx, item_to_buy in enumerate(items_to_buy):
            overview_item = overview_items[idx]
            self.compare(idx, item_to_buy, overview_item)


if __name__ == "__main__":
    unittest.main()
