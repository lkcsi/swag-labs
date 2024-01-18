import database.database as database
from parameterized import parameterized_class
import unittest
from pages import CartItem, InventoryPage, CartPage, LoginPage
import pytest
from utilities import params_from_json as params


class TestCart:

    @pytest.mark.usefixtures("setup", "login_page", "inventory_page", "cart_page", "header")
    @pytest.mark.parametrize("username,password", params("../testdata/valid_credentials.json"))
    def test_cart_content_from_inventory(self, username, password):
        self.login_page.login(username, password)
        inventory_items = self.inventory_page.get_items()
        items_to_buy = []
        for idx, item in enumerate(inventory_items):
            self.inventory_page.add_item(idx)
            items_to_buy.append(item)
            self.header.click_cart()
            assert items_to_buy == self.cart_page.items()
            self.cart_page.continue_shopping()

    @pytest.mark.usefixtures("setup", "login_page", "inventory_page", "cart_page", "header", "details_page")
    @pytest.mark.parametrize("username,password", params("../testdata/valid_credentials.json"))
    def test_cart_content_from_details(self, username, password):
        self.login_page.login(username, password)
        inventory_items = self.inventory_page.get_items()
        items_to_buy = []
        for item in inventory_items:
            item.click_image()
            self.details_page.add_item()
            items_to_buy.append(item)
            self.header.click_cart()
            assert items_to_buy == self.cart_page.items()
            self.cart_page.continue_shopping()

    @pytest.mark.usefixtures("setup", "login_page", "inventory_page", "cart_page", "header")
    @pytest.mark.parametrize("username,password", params("../testdata/valid_credentials.json"))
    def test_cart_remove(self, username, password):
        self.login_page.login(username, password)
        items_to_buy = self.inventory_page.get_items()
        self.inventory_page.add_all_item()
        self.header.click_cart()
        items_in_cart = self.cart_page.items()

        assert items_to_buy == items_in_cart

        for item in items_in_cart:
            item.click_remove()
            items_to_buy.pop(0)
            assert items_to_buy == self.cart_page.items()


if __name__ == "__main__":
    unittest.main()
