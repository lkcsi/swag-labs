import pytest
from utilities import params_from_json as params
from base import BaseTest


class TestCartContent(BaseTest):

    @pytest.mark.usefixtures("setup")
    @pytest.mark.parametrize("username,password", params("testdata/valid_credentials.json"))
    def test_cart_content_from_inventory(self, username, password):
        inventory_page = self.login_page.login(username, password)
        items_to_buy = []
        for item in inventory_page:
            item.click_add()
            items_to_buy.append(item)
            cart_page = self.header.click_cart()
            self.check_content(items_to_buy, cart_page.get_items())
            cart_page.continue_shopping()

    @pytest.mark.usefixtures("setup")
    @pytest.mark.parametrize("username,password", params("testdata/valid_credentials.json"))
    def test_cart_content_from_details(self, username, password):
        inventory_page = self.login_page.login(username, password)
        items_to_buy = []
        for item in inventory_page:
            details_page = item.click_image()
            details_page.add_item()
            items_to_buy.append(item)
            cart_page = self.header.click_cart()
            self.check_content(items_to_buy, cart_page.get_items())
            cart_page.continue_shopping()

    @pytest.mark.usefixtures("setup")
    @pytest.mark.parametrize("username,password", params("testdata/valid_credentials.json"))
    def test_cart_remove(self, username, password):
        inventory_page = self.login_page.login(username, password)
        items_to_buy = inventory_page.get_items()
        inventory_page.add_all_items()
        cart_page = self.header.click_cart()
        items_in_cart = cart_page.get_items()

        self.check_content(items_to_buy, items_in_cart)

        for item in items_in_cart:
            item.click_remove()
            items_to_buy.pop(0)
            self.check_content(items_to_buy, cart_page.get_items())

    @staticmethod
    def check_content(selected_items, cart_items):
        assert selected_items == cart_items, "cart content doesn't match selected items"
