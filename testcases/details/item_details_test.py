import pytest
from testcases import BaseTest


class TestItemDetails(BaseTest):

    """
    Steps:
     * navigate to inventory page
     * for each item in inventory page:
     ** click item image / title
     ** check item details
     ** click Back to products button
    """

    @pytest.mark.usefixtures("setup")
    def test_details_open_with_image(self):
        inventory_page = self.login()
        self.open_with(lambda x: x.click_title(), inventory_page)

    @pytest.mark.usefixtures("setup")
    def test_details_open_with_title(self):
        inventory_page = self.login()
        self.open_with(lambda x: x.click_image(), inventory_page)

    @staticmethod
    def open_with(click, inventory_page):
        for item in inventory_page:
            details_page = click(item)
            assert details_page.get_item() == item, "item details should match the selected item"
            details_page.back_to_products()
