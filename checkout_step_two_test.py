import unittest
from base_test import BaseTestCase
from parameterized.parameterized import parameterized_class
from database.database import users

TAX = 1.08


@parameterized_class(users())
class OverViewTestCase(BaseTestCase):
    def test_cancel_step_two(self):
        self.login()
        self.add_inventory_item(0)
        self.click_cart()
        self.click_checkout()
        self.fill_billing_info()
        self.continue_to_step_two()
        self.cancel_step_two()

    def test_complete(self):
        self.login()
        self.add_all_items()
        self.click_cart()
        self.click_checkout()
        self.fill_billing_info()
        self.continue_to_step_two()
        self.checkout_two_page.finish_button.click()

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

        actual = self.checkout_two_page.subtotal
        actual = OverViewTestCase.convert_to_float(actual)

        self.assertEqual(expected, actual)

        expected = expected * TAX
        actual = self.checkout_two_page.total
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

        overview_items = self.checkout_two_page.get_items()

        self.compare_all_items(items_to_buy, overview_items)


if __name__ == "__main__":
    unittest.main()
