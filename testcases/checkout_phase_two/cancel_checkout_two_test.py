import pytest
from pages import InventoryPage, CheckoutTwoPage
from testcases import BaseTest


class TestCancelCheckoutTwo(BaseTest):

    """
    Steps:
     * navigate to checkout two page
     * click Cancel button
     * check landing page
    """

    @pytest.mark.usefixtures("setup")
    def test_cancel_checkout_two(self):
        checkout_two_page = self.go_to_checkout_two(False, 0)
        checkout_two_page.cancel()
        assert self.header.get_title() == InventoryPage.TITLE, "landed on wrong page after cancellation"
