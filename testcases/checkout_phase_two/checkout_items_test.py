import pytest
from base import BaseTest


class TestCheckoutItems(BaseTest):

    @pytest.mark.usefixtures("setup")
    def test_overview_items(self):
        inventory_page = self.login()
        inventory_page.add_all_items()

        items_to_buy = inventory_page.get_items()
        cart_page = self.header.click_cart()
        checkout_one_page = cart_page.checkout()
        checkout_two_page = checkout_one_page.fill_and_continue()

        overview_items = checkout_two_page.get_items()

        assert items_to_buy == overview_items, "items in overview not match with selected items"
