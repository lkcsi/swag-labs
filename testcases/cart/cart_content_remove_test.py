import pytest
from testcases import BaseTest


class TestCartContentRemove(BaseTest):

    @pytest.mark.usefixtures("setup")
    def test_cart_remove(self):
        inventory_page = self.login()
        items_to_buy = inventory_page.get_items()
        inventory_page.add_all_items()
        cart_page = self.header.click_cart()
        items_in_cart = cart_page.get_items()

        assert items_in_cart == items_to_buy, "cart content doesn't match selected items"

        for item in items_in_cart:
            item.click_remove()
            items_to_buy.pop(0)

            assert cart_page.get_items() == items_to_buy, "cart content doesn't match removed items"
