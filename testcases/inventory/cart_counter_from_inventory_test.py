import pytest
from testcases import BaseTest


class TestCartCounterFromInventory(BaseTest):

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
