import pytest

from pages import CheckoutOnePage
from utilities import params_from_json as params
from base import BaseTest


class TestCheckoutInvalidInfo(BaseTest):

    @pytest.mark.xfail
    @pytest.mark.usefixtures("setup")
    @pytest.mark.parametrize("first_name,last_name,postal_code,invalid_field",
                             params("testdata/invalid_checkout_info.json"))
    def test_invalid_input(self, first_name, last_name, postal_code, invalid_field):
        inventory_page = self.login()
        inventory_page.add_all_items()
        cart_page = self.header.click_cart()
        checkout_one_page = cart_page.checkout()
        checkout_one_page.fill_and_continue(first_name, last_name, postal_code)

        assert checkout_one_page.error_text != "", "no error message when using invalid inputs"
        assert self.header.get_title() == CheckoutOnePage.TITLE, f"proceed with wrong {invalid_field}"
