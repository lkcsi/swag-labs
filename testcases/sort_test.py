import pytest
from pages import SortBy
from base import ImageItem
from utilities import params_from_json as params


class TestSort:

    @pytest.mark.usefixtures("driver", "login_page", "header")
    @pytest.mark.parametrize("username,password", params("../testdata/valid_credentials.json"))
    def test_order_az(self, username, password):
        inventory_page = self.login_page.login(username, password)
        self.order_by(inventory_page, SortBy.AZ, lambda x: x.title)

    @pytest.mark.usefixtures("driver", "login_page", "header")
    @pytest.mark.parametrize("username,password", params("../testdata/valid_credentials.json"))
    def test_order_price_low_to_high(self, username, password):
        inventory_page = self.login_page.login(username, password)
        self.order_by(inventory_page, SortBy.LOHI, lambda x: x.price)

    @pytest.mark.usefixtures("driver", "login_page", "header")
    @pytest.mark.parametrize("username,password", params("../testdata/valid_credentials.json"))
    def test_order_price_high_to_low(self, username, password):
        inventory_page = self.login_page.login(username, password)
        self.order_by(inventory_page, SortBy.HILO, lambda x: x.price, True)

    @pytest.mark.usefixtures("driver", "login_page", "header")
    @pytest.mark.parametrize("username,password", params("../testdata/valid_credentials.json"))
    def test_order_za(self, username, password):
        inventory_page = self.login_page.login(username, password)
        self.order_by(inventory_page, SortBy.ZA, lambda x: x.title, True)

    def order_by(self, inventory_page, by: SortBy, by_func, reverse=False):
        inventory_page.sort(by)

        items_in_order = inventory_page.get_items()
        items_in_order.sort(key=by_func, reverse=reverse)

        self.compare_order(items_in_order, inventory_page.get_items(), by_func)

    @staticmethod
    def compare_order(expected_items: list[ImageItem], actual_items: list[ImageItem], by_func):
        expected_items = [by_func(i) for i in expected_items]
        actual_items = [by_func(i) for i in actual_items]

        assert actual_items == expected_items
