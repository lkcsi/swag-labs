import pytest
from utilities import params_from_json as params
from base_test import BaseTest


class TestCartCounter(BaseTest):

    @pytest.mark.usefixtures("setup")
    @pytest.mark.parametrize("username,password", params("../testdata/valid_credentials.json"))
    def test_cart_counter_from_details(self, username, password):
        expected = 0

        inventory_page = self.login_page.login(username, password)
        self.check_counter(expected)

        for item in inventory_page:
            expected += 1
            details_page = item.click_image()
            details_page.add_item()
            self.check_counter(expected)
            details_page.back_to_products()

        for item in inventory_page:
            expected -= 1
            details_page = item.click_image()
            details_page.remove_item()
            self.check_counter(expected)
            details_page.back_to_products()

    def check_counter(self, expected):
        assert expected == self.header.cart.counter(), "cart counter is not correct according to the selected items"

    @pytest.mark.usefixtures("setup")
    @pytest.mark.parametrize("username,password", params("../testdata/valid_credentials.json"))
    def test_cart_counter_from_inventory(self, username, password):
        expected = 0

        inventory_page = self.login_page.login(username, password)
        self.check_counter(expected)

        for item in inventory_page:
            expected += 1
            item.click_add()
            self.check_counter(expected)

        for item in inventory_page:
            expected -= 1
            item.click_remove()
            self.check_counter(expected)
