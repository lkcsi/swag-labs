import pytest
from testcases import BaseTest


class TestCartCounterFromInventory(BaseTest):

    """
    Steps:
     * navigate to inventory page
     * for each item in inventory page:
     ** click Add to cart button
     ** check cart counter
     * for each item in inventory page:
     ** click Remove button
     ** check cart counter
    """

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
