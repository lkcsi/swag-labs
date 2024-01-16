import unittest
from base_test import BaseTestCase

TAX = 1.08


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

        self.assertEqual(self.complete_page.TITLE, self.get_title())

        self.complete_page.back_home_button.click()

        self.assertEqual(self.inventory_page.TITLE, self.get_title())

    def test_totals(self):
        self.login()
        self.add_all_items()

        items_to_buy = self.inventory_page.get_items()

        self.click_cart()
        self.click_checkout()
        self.fill_billing_info()

        expected = 0
        for item in items_to_buy:
            expected += item.price

        actual = self.overview_page.subtotal
        actual = OverViewTestCase.convert_to_float(actual)

        self.assertEqual(expected, actual)

        expected = expected * TAX
        actual = self.overview_page.total
        actual = OverViewTestCase.convert_to_float(actual)

        self.assertAlmostEqual(expected, actual, 2)

    @staticmethod
    def convert_to_float(text: str) -> float:
        text = text.split("$")[1]
        return float(text)

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
