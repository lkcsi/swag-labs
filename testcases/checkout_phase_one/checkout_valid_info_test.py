import pytest

from pages import CheckoutTwoPage
from utilities import params_from_json as params
from testcases import BaseTest


class TestCheckoutValidInfo(BaseTest):

    """
    Steps:
     * navigate to checkout one page
     * fill shipping info with valid values
     * click Continue button
     * check landing page
    """

    @pytest.mark.usefixtures("setup")
    @pytest.mark.parametrize("first_name,last_name,postal_code", params("testdata/valid_checkout_info.json"))
    def test_checkout_with_valid_info(self, first_name, last_name, postal_code):
        checkout_one_page = self.go_to_checkout_one(add_all=True)
        checkout_one_page.fill_and_continue(first_name, last_name, postal_code)

        assert self.header.get_title() == CheckoutTwoPage.TITLE, "landed wrong page after submit"
        assert checkout_one_page.error_text == "", "error message when using valid inputs"
