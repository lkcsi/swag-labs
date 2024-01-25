import pytest
from testcases import BaseTest


class TestCartContentFromDetails(BaseTest):

    """
    Steps:
     * navigate to inventory page
     * for each item in inventory:
     ** click item image
     ** click Add to cart Button
     ** click Cart Icon
     ** check Cart content
     ** click Continue Shopping button
    """

    @pytest.mark.usefixtures("setup")
    def test_cart_content_from_details(self):
        inventory_page = self.login()
        items_to_buy = []
        for item in inventory_page:
            details_page = item.click_image()
            details_page.add_item()
            items_to_buy.append(item)
            cart_page = self.header.click_cart()
            self.check_content(items_to_buy, cart_page.get_items())
            cart_page.continue_shopping()

    @staticmethod
    def check_content(selected_items, cart_items):
        assert cart_items == selected_items, "cart content doesn't match selected items from details page"
