import pytest
from base import BaseTest


class TestItemDetails(BaseTest):

    @pytest.mark.usefixtures("setup")
    def test_open_with_image(self):
        inventory_page = self.login()
        self.open_with(lambda x: x.click_title(), inventory_page)

    @pytest.mark.usefixtures("setup")
    def test_open_with_title(self):
        inventory_page = self.login()
        self.open_with(lambda x: x.click_image(), inventory_page)

    @staticmethod
    def open_with(click, inventory_page):
        for item in inventory_page:
            details_page = click(item)
            assert details_page.get_item() == item, "item details should match the selected item"
            details_page.back_to_products()
