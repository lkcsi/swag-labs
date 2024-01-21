import pytest
from pages import SortBy
from base import ImageItem, BaseTest
from utilities import params_from_json as params


class TestSort(BaseTest):

    @pytest.mark.usefixtures("setup")
    def test_order_az(self):
        self.order_by(SortBy.AZ, lambda x: x.title)

    @pytest.mark.usefixtures("setup")
    def test_order_price_low_to_high(self):
        self.order_by(SortBy.LOHI, lambda x: x.price)

    @pytest.mark.usefixtures("setup")
    def test_order_price_high_to_low(self):
        self.order_by(SortBy.HILO, lambda x: x.price, True)

    @pytest.mark.usefixtures("setup")
    def test_order_za(self):
        self.order_by(SortBy.ZA, lambda x: x.title, True)

    def order_by(self, by: SortBy, field, reverse=False):
        inventory_page = self.login()
        items_in_order = inventory_page.get_items()

        inventory_page.sort(by)
        items_in_order.sort(key=field, reverse=reverse)

        self.compare_order(items_in_order, inventory_page.get_items(), field)

    @staticmethod
    def compare_order(expected_items: list[ImageItem], actual_items: list[ImageItem], by_func):
        expected_items = [by_func(i) for i in expected_items]
        actual_items = [by_func(i) for i in actual_items]

        assert actual_items == expected_items
