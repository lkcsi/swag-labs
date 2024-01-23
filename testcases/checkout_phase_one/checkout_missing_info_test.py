import pytest

from pages import CheckoutOnePage
from utilities import params_from_json as params
from base import BaseTest


class TestCheckoutMissingInfo(BaseTest):

    @pytest.mark.usefixtures("setup")
    @pytest.mark.parametrize("first_name,last_name,postal_code, missing_field",
                             params("testdata/missing_checkout_info.json"))
    def test_missing_input(self, first_name, last_name, postal_code, missing_field):
        checkout_one_page = self.go_to_checkout_one(add_all=True)
        checkout_one_page.fill_and_continue(first_name, last_name, postal_code)

        assert f"{missing_field} is required" in checkout_one_page.error_text
        assert self.header.get_title() == CheckoutOnePage.TITLE, f"proceed with missing {missing_field}"
