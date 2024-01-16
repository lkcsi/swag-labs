import unittest
from base_test import BaseTestCase
from pages.header import SecondaryHeader, Cart
from parameterized import parameterized
from parameterized.parameterized import parameterized_class
from database.database import users


@parameterized_class(users())
class CheckoutTestCase(BaseTestCase):
    def test_cancel_step_one(self):
        self.login()
        self.add_inventory_item(0)
        self.click_cart()
        self.click_checkout()
        self.fill_billing_info()
        self.cancel_step_one()

    def test_successful(self):
        self.proceed("test_name", "test_name", 8888)
        self.check_success()

    @parameterized.expand(
        [
            ["", "last_name", 8888, "First Name"],
            ["first_name", "", 8888, "Last Name"],
            ["first_name", "last_name", "", "Postal Code"],
        ]
    )
    def test_missing_input(self, first_name, last_name, postal_code, input_field):
        self.proceed(first_name, last_name, postal_code)
        self.check_missing(input_field)

    @parameterized.expand(
        [
            ["!@#$%^", "last_name", 8888],
            ["first_name", "!@#$%^", 8888],
            ["first_name", "last_name", "!@#$%^"],
        ]
    )
    def test_wrong_input(self, first_name, last_name, postal_code):
        self.proceed(first_name, last_name, postal_code)
        self.check_wrong()

    def check_missing(self, input_field):
        self.assertTrue(
            f"{input_field} is required" in self.checkout_one_page.error_text,
            f"Error message should be: {input_field} is required",
        )

    def check_wrong(self):
        self.assertTrue(
            self.checkout_one_page.error_text != "",
            "Error message should appeared with invalid input",
        )

    def proceed(self, first_name, last_name, postal_code):
        self.login()
        self.add_all_items()
        self.click_cart()
        self.click_checkout()

        self.checkout_one_page.first_name = first_name
        self.checkout_one_page.last_name = last_name
        self.checkout_one_page.postal_code = postal_code

        self.checkout_one_page.continue_button.click()

    def check_success(self):
        header = SecondaryHeader(self.driver)
        self.assertEqual(
            self.checkout_two_page.TITLE,
            header.title(),
            f"Should proceed with valid input, error: {self.checkout_one_page.error_text}",
        )


if __name__ == "__main__":
    unittest.main()
