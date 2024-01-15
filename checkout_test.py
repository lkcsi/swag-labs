import unittest
from base_test import BaseTestCase
from pages.header import SecondaryHeader, Cart


class CheckoutTestCase(BaseTestCase):
    username = "standard_user"
    password = "secret_sauce"

    def test_successful(self):
        self.proceed("test_name", "test_name", "8888")

    def test_missing_firstname(self):
        self.proceed("", "test_name", "8888")
        self.check_error("First Name")

    def test_missing_lastname(self):
        self.proceed("test_name", "", "8888")
        self.check_error("Last Name")

    def test_missing_postcode(self):
        self.proceed("test_name", "test_name", "")
        self.check_error("Postal Code")

    def proceed(self, first_name, last_name, postal_code):
        self.login()
        self.add_all_items()
        self.click_cart()
        self.click_checkout()

        self.checkout_page.first_name = first_name
        self.checkout_page.last_name = last_name
        self.checkout_page.postal_code = postal_code

        self.checkout_page.continue_button.click()

    def check_error(self, info):
        header = SecondaryHeader(self.driver)
        self.assertEqual("Checkout: Your Information", header.title())
        self.assertTrue(f"{info} is required" in self.checkout_page.error_text)

    def check_success(self):
        header = SecondaryHeader(self.driver)
        self.assertEqual("Checkout: Overview", header.title())


if __name__ == "__main__":
    unittest.main()
