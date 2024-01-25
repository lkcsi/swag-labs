import pytest
from pages import InventoryPage, CheckoutTwoPage
from testcases import BaseTest


class TestCancelCheckout(BaseTest):

    @pytest.mark.usefixtures("setup")
    def test_cancel_checkout_two(self):
        checkout_two_page = self.go_to_checkout_two(False, 0)

        assert self.header.get_title() == CheckoutTwoPage.TITLE, "wrong page before cancel checkout"
        checkout_two_page.cancel()
        assert self.header.get_title() == InventoryPage.TITLE, "landed on wrong page after cancellation"
