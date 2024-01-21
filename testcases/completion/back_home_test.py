import pytest

from base import BaseTest
from utilities import params_from_json as params
from pages import InventoryPage


class TestCompletion(BaseTest):

    @pytest.mark.usefixtures("setup")
    def test_back_home(self):
        inventory_page = self.login()
        inventory_page.add_all_items()

        cart_page = self.header.click_cart()
        checkout_one = cart_page.checkout()
        checkout_two = checkout_one.fill_and_continue()
        complete_page = checkout_two.finish()
        complete_page.back_to_home()

        assert InventoryPage.TITLE == self.header.get_title(), "landed wrong page after completion"
        assert self.header.cart.counter() == 0, "selected items are not 0 after completion"
