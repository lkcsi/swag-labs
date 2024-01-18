import pytest
from utilities import params_from_json as params


class TestItemDetails:

    @pytest.mark.usefixtures("driver", "login_page", "header")
    @pytest.mark.parametrize("username,password", params("../testdata/valid_credentials.json"))
    def test_open_with_image(self, username, password):
        inventory_page = self.login_page.login(username, password)
        self.open_with(lambda x: x.click_title(), inventory_page)

    @pytest.mark.usefixtures("driver", "login_page", "header")
    @pytest.mark.parametrize("username,password", params("../testdata/valid_credentials.json"))
    def test_open_with_title(self, username, password):
        inventory_page = self.login_page.login(username, password)
        self.open_with(lambda x: x.click_image(), inventory_page)

    @staticmethod
    def open_with(click, inventory_page):
        page_items = inventory_page.get_items()
        for idx, item in enumerate(page_items):
            details_page = click(item)
            assert details_page.get_item() == item
            details_page.back_to_products()
