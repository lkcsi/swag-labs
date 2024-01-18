import pytest
from utilities import params_from_json as params
from pages import CartPage, InventoryPage


class TestCancelCheckout:

    @pytest.mark.usefixtures("driver", "login_page", "header")
    @pytest.mark.parametrize("username,password", params("../testdata/valid_credentials.json"))
    def test_cancel_checkout_one(self, username, password):
        inventory_page = self.login_page.login(username, password)
        inventory_page.add_item(0)
        cart_page = self.header.click_cart()
        checkout_one_page = cart_page.checkout()
        checkout_one_page.fill_info("John", "McClain", 8888)
        checkout_one_page.cancel()

        assert CartPage.TITLE == self.header.get_title(), "landed wrong page after cancel checkout"

    @pytest.mark.usefixtures("driver", "login_page", "header")
    @pytest.mark.parametrize("username,password", params("../testdata/valid_credentials.json"))
    def test_cancel_checkout_two(self, username, password):
        inventory_page = self.login_page.login(username, password)
        inventory_page.add_item(0)

        cart_page = self.header.click_cart()
        checkout_one_page = cart_page.checkout()
        checkout_two_page = checkout_one_page.fill_and_continue()
        checkout_two_page.cancel()

        assert InventoryPage.TITLE == self.header.get_title(), "landed on wrong page after cancellation"
