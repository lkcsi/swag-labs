import pytest
from utilities import params_from_json as params
from base import BaseTest


class TestCheckoutItems(BaseTest):

    @pytest.mark.usefixtures("setup")
    @pytest.mark.parametrize("username,password", params("testdata/valid_credentials.json"))
    def test_overview_items(self, username, password):
        inventory_page = self.login_page.login(username, password)
        inventory_page.add_all_items()

        items_to_buy = inventory_page.get_items()
        cart_page = self.header.click_cart()
        checkout_one_page = cart_page.checkout()
        checkout_two_page = checkout_one_page.fill_and_continue()

        overview_items = checkout_two_page.get_items()

        assert items_to_buy == overview_items, "items in overview not match with selected items"
