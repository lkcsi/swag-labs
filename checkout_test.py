import unittest
from base_test import BaseTestCase
from pages.header import SecondaryHeader, Cart
from parameterized import parameterized


class CheckoutTestCase(BaseTestCase):
    username = "standard_user"
    password = "secret_sauce"

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

    def proceed(self, first_name, last_name, postal_code):
        self.login()
        self.add_all_items()
        self.click_cart()
        self.click_checkout()

        self.checkout_page.first_name = first_name
        self.checkout_page.last_name = last_name
        self.checkout_page.postal_code = postal_code

        self.checkout_page.continue_button.click()

    def check_missing(self, input_field):
        header = SecondaryHeader(self.driver)
        self.assertEqual(
            self.checkout_page.TITLE,
            header.title(),
            "Should not proceed with missing input",
        )
        self.assertTrue(f"{input_field} is required" in self.checkout_page.error_text)

    def check_wrong(self, input_value):
        header = SecondaryHeader(self.driver)
        self.assertEqual(
            self.checkout_page.TITLE,
            header.title(),
            f"Should not proceed with invalid input {input_value}",
        )
        self.assertTrue(self.checkout_page.error_text is not "")

    def check_success(self):
        header = SecondaryHeader(self.driver)
        self.assertEqual(
            self.overview_page.TITLE, header.title(), "Should proceed with valid input"
        )


if __name__ == "__main__":
    unittest.main()
