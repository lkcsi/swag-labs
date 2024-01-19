import pytest

from pages import CheckoutTwoPage, CheckoutOnePage
from utilities import params_from_json as params
from base import BaseTest


class TestCheckoutInfo(BaseTest):

    @pytest.mark.usefixtures("setup")
    @pytest.mark.parametrize("username,password", params("testdata/valid_credentials.json"))
    @pytest.mark.parametrize("first_name,last_name,postal_code", params("testdata/valid_checkout_info.json"))
    def test_with_valid_info(self, username, password, first_name, last_name, postal_code):
        inventory_page = self.login_page.login(username, password)
        inventory_page.add_all_items()
        cart_page = self.header.click_cart()
        checkout_one_page = cart_page.checkout()
        checkout_one_page.fill_and_continue(first_name, last_name, postal_code)
        self.check_success(checkout_one_page)

    @pytest.mark.usefixtures("driver", "login_page", "header")
    @pytest.mark.parametrize("username,password", params("testdata/valid_credentials.json"))
    @pytest.mark.parametrize("first_name,last_name,postal_code, missing_field",
                             params("testdata/missing_checkout_info.json"))
    def test_missing_input(self, username, password, first_name, last_name, postal_code, missing_field):
        inventory_page = self.login_page.login(username, password)
        inventory_page.add_all_items()
        cart_page = self.header.click_cart()
        checkout_one_page = cart_page.checkout()
        checkout_one_page.fill_and_continue(first_name, last_name, postal_code)
        self.check_missing(missing_field, checkout_one_page)

    @pytest.mark.xfail("there is no such requirement to check invalid characters yet")
    @pytest.mark.usefixtures("driver", "login_page", "header")
    @pytest.mark.parametrize("username,password", params("testdata/valid_credentials.json"))
    @pytest.mark.parametrize("first_name,last_name,postal_code,invalid_field",
                             params("testdata/invalid_checkout_info.json"))
    def test_invalid_input(self, username, password, first_name, last_name, postal_code, invalid_field):
        inventory_page = self.login_page.login(username, password)
        inventory_page.add_all_items()
        cart_page = self.header.click_cart()
        checkout_one_page = cart_page.checkout()
        checkout_one_page.fill_and_continue(first_name, last_name, postal_code)
        self.check_wrong(invalid_field, checkout_one_page)

    def check_missing(self, missing_field, checkout_one_page):
        assert f"{missing_field} is required" in checkout_one_page.error_text
        assert CheckoutOnePage.TITLE == self.header.get_title(), f"proceed with missing {missing_field}"

    def check_wrong(self, invalid_field, checkout_one_page):
        assert checkout_one_page.error_text != "", "no error message when using invalid inputs"
        assert CheckoutOnePage.TITLE == self.header.get_title(), f"proceed with wrong {invalid_field}"

    def check_success(self, checkout_one_page):
        assert CheckoutTwoPage.TITLE == self.header.get_title(), "landed wrong page after submit"
        assert checkout_one_page.error_text != "", "error message when using valid inputs"
