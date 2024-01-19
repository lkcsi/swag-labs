import pytest
from pages import SortBy
from base import ImageItem
from utilities import params_from_json as params
from base_test import BaseTest


class TestSort(BaseTest):

    @pytest.mark.usefixtures("setup")
    @pytest.mark.parametrize("username,password", params("../testdata/valid_credentials.json"))
    def test_order_az(self, username, password):
        self.order_by(username, password, SortBy.AZ, lambda x: x.title)

    @pytest.mark.usefixtures("setup")
    @pytest.mark.parametrize("username,password", params("../testdata/valid_credentials.json"))
    def test_order_price_low_to_high(self, username, password):
        self.order_by(username, password, SortBy.LOHI, lambda x: x.price)

    @pytest.mark.usefixtures("driver", "login_page", "header")
    @pytest.mark.parametrize("username,password", params("../testdata/valid_credentials.json"))
    def test_order_price_high_to_low(self, username, password):
        self.order_by(username, password, SortBy.HILO, lambda x: x.price, True)

    @pytest.mark.usefixtures("setup", "login_page", "header")
    @pytest.mark.parametrize("username,password", params("../testdata/valid_credentials.json"))
    def test_order_za(self, username, password):
        self.order_by(username, password, SortBy.ZA, lambda x: x.title, True)

    def order_by(self, username, password, by: SortBy, field, reverse=False):
        inventory_page = self.login_page.login(username, password)
        items_in_order = inventory_page.get_items()

        inventory_page.sort(by)
        items_in_order.sort(key=field, reverse=reverse)

        self.compare_order(items_in_order, inventory_page.get_items(), field)

    @staticmethod
    def compare_order(expected_items: list[ImageItem], actual_items: list[ImageItem], by_func):
        expected_items = [by_func(i) for i in expected_items]
        actual_items = [by_func(i) for i in actual_items]

        assert actual_items == expected_items
