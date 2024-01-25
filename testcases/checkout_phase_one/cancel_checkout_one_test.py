import pytest
from pages import CartPage, CheckoutOnePage
from testcases import BaseTest


class TestCancelCheckoutOne(BaseTest):

    @pytest.mark.usefixtures("setup")
    def test_cancel_checkout_one(self):
        checkout_one_page = self.go_to_checkout_one(add_all=True)
        checkout_one_page.fill_info("John", "McClain", 8888)

        assert self.header.get_title() == CheckoutOnePage.TITLE, "wrong page before cancel checkout"
        checkout_one_page.cancel()
        assert self.header.get_title() == CartPage.TITLE, "landed wrong page after cancel checkout"
