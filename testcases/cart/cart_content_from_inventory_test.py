import pytest
from testcases import BaseTest


class TestCartContentFromInventory(BaseTest):

    """
    Steps:
     * navigate to inventory page
     * for each item in inventory:
     ** click Add to cart button
     ** click Cart icon
     ** check Cart content
     ** click Continue Shopping button
    """

    @pytest.mark.usefixtures("setup")
    def test_cart_content_from_inventory(self):
        inventory_page = self.login()
        items_to_buy = []
        for item in inventory_page:
            item.click_add()
            items_to_buy.append(item)
            cart_page = self.header.click_cart()
            self.check_content(items_to_buy, cart_page.get_items())
            cart_page.continue_shopping()

    @staticmethod
    def check_content(selected_items, cart_items):
        assert cart_items == selected_items, "cart content doesn't match selected items from inventory"
