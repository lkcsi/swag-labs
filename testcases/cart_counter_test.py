import pytest
from utilities import params_from_json as params


class TestCartCounter:

    @pytest.mark.usefixtures("driver", "login_page", "header")
    @pytest.mark.parametrize("username,password", params("../testdata/valid_credentials.json"))
    def test_cart_counter_from_details(self, username, password):
        expected = 0

        inventory_page = self.login_page.login(username, password)
        self.check_counter(expected, self.header)

        for item in inventory_page.get_items():
            expected += 1
            details_page = item.click_image()
            details_page.add_item()
            self.check_counter(expected, self.header)
            details_page.back_to_products()

        for item in inventory_page.get_items():
            expected -= 1
            details_page = item.click_image()
            details_page.remove_item()
            self.check_counter(expected, self.header)
            details_page.back_to_products()

    @staticmethod
    def check_counter(expected, header):
        assert expected == header.cart.counter(), "cart counter is not correct according to the selected items"

    @pytest.mark.usefixtures("driver", "login_page", "header")
    @pytest.mark.parametrize("username,password", params("../testdata/valid_credentials.json"))
    def test_cart_counter_from_inventory(self, username, password):
        expected = 0

        inventory_page = self.login_page.login(username, password)
        self.check_counter(expected, self.header)

        for item in inventory_page.get_items():
            expected += 1
            item.click_add()
            self.check_counter(expected, self.header)

        for item in inventory_page.get_items():
            expected -= 1
            item.click_remove()
            self.check_counter(expected, self.header)
