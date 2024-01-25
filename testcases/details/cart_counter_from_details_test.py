import pytest
from testcases import BaseTest


class TestCartCounterFromDetails(BaseTest):

    """
    Steps:
     * navigate to inventory page
     * for each item in inventory page:
     ** click item image
     ** click Add to cart button
     ** check cart counter
     ** click Back to products button
     * for each item in inventory page:
     ** click item image
     ** click Remove button
     ** check cart counter
     ** click Back to products button
    """

    @pytest.mark.usefixtures("setup")
    def test_cart_counter_from_details(self):
        expected = 0

        inventory_page = self.login()
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
