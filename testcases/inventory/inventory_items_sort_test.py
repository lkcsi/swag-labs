import pytest
from pages import SortBy
from testcases import BaseTest
from pages.elements import Item
from selenium.common.exceptions import NoAlertPresentException


class TestSort(BaseTest):

    """
    Steps:
     * login and navigate to inventory page
     * click to sort drop down
     * select Name (A to Z) / Name (Z to A) / Price (low to high) / Price (high to low)
     * check items order
    """

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
        self.handle_alert()
        items_in_order.sort(key=field, reverse=reverse)

        self.compare_order(items_in_order, inventory_page.get_items(), field)

    def handle_alert(self):
        try:
            alert = self.driver.switch_to.alert
            alert_message = alert.text
            alert.accept()
        except NoAlertPresentException:
            alert_message = ""

        assert alert_message == ""

    @staticmethod
    def compare_order(expected_items: list[Item], actual_items: list[Item], by_func):
        expected_items = [by_func(i) for i in expected_items]
        actual_items = [by_func(i) for i in actual_items]

        assert actual_items == expected_items
