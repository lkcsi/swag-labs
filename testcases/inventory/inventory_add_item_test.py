import pytest
from utilities import params_from_json as params
from base import BaseTest


class TestAddItem(BaseTest):

    @pytest.mark.usefixtures("setup")
    def test_inventory_add_item(self):
        inventory_page = self.login()
        selected_items = []
        for item in inventory_page:
            selected_items.append(item)
            item.click_add()
        assert inventory_page.get_selected_items() == selected_items
