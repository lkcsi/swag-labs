import pytest
from utilities import params_from_json as params
from pages import CartPage, InventoryPage, CheckoutOnePage, CheckoutTwoPage
from base import BaseTest


class TestCancelCheckout(BaseTest):

    @pytest.mark.usefixtures("setup")
    def test_cancel_checkout_phase_one(self):
        inventory_page = self.login()
        inventory_page.add_item(0)
        cart_page = self.header.click_cart()
        checkout_one_page = cart_page.checkout()
        checkout_one_page.fill_info("John", "McClain", 8888)

        assert self.header.get_title() == CheckoutOnePage.TITLE, "wrong page before cancel checkout"
        checkout_one_page.cancel()
        assert self.header.get_title() == CartPage.TITLE, "landed wrong page after cancel checkout"
