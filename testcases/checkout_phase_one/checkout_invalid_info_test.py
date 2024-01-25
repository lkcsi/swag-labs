import pytest

from pages import CheckoutOnePage
from utilities import params_from_json as params
from testcases import BaseTest


class TestCheckoutInvalidInfo(BaseTest):

    """
    Steps:
     * navigate to checkout one page
     * fill shipping info with invalid values
     * click Continue button
     * check error message
    """

    @pytest.mark.xfail
    @pytest.mark.usefixtures("setup")
    @pytest.mark.parametrize("first_name,last_name,postal_code,invalid_field",
                             params("testdata/invalid_checkout_info.json"))
    def test_checkout_invalid_input(self, first_name, last_name, postal_code, invalid_field):
        checkout_one_page = self.go_to_checkout_one(add_all=True)
        checkout_one_page.fill_and_continue(first_name, last_name, postal_code)

        assert checkout_one_page.error_text != "", "no error message when using invalid inputs"
        assert self.header.get_title() == CheckoutOnePage.TITLE, f"proceed with wrong {invalid_field}"
