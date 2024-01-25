import pytest
from testcases import BaseTest


class TestCheckoutItemsOverview(BaseTest):

    """
    Steps:
     * navigate to inventory page
     * add all items
     * navigate to checkout two page
     * check overview items match with selected items
    """

    @pytest.mark.usefixtures("setup")
    def test_checkout_items_overview(self):
        inventory_page = self.login()
        inventory_page.add_all_items()

        items_to_buy = inventory_page.get_items()
        cart_page = self.header.click_cart()
        checkout_one_page = cart_page.checkout()
        checkout_two_page = checkout_one_page.fill_and_continue()

        overview_items = checkout_two_page.get_items()

        assert items_to_buy == overview_items, "items in overview not match with selected items"
