import pytest
from pages import InventoryPage, CheckoutTwoPage
from base import BaseTest


class TestCancelCheckout(BaseTest):

    @pytest.mark.usefixtures("setup")
    def test_cancel_checkout_two(self):
        inventory_page = self.login()
        inventory_page.add_item(0)

        cart_page = self.header.click_cart()
        checkout_one_page = cart_page.checkout()
        checkout_two_page = checkout_one_page.fill_and_continue()

        assert self.header.get_title() == CheckoutTwoPage.TITLE, "wrong page before cancel checkout"
        checkout_two_page.cancel()
        assert self.header.get_title() == InventoryPage.TITLE, "landed on wrong page after cancellation"
