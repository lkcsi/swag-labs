import pytest
from utilities import params_from_json as params
from base import BaseTest


class TestCartCounter(BaseTest):

    @pytest.mark.usefixtures("setup")
    def test_cart_counter_from_inventory(self):
        expected = 0

        inventory_page = self.login()
        self.check_counter(expected)

        for item in inventory_page:
            expected += 1
            item.click_add()
            self.check_counter(expected)

        for item in inventory_page:
            expected -= 1
            item.click_remove()
            self.check_counter(expected)
