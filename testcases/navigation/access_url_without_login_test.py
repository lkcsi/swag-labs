import pytest
from pages.inventory_page import InventoryPage
from testcases import BaseTest
from utilities import params_from_json as params


class TestAccessUrlWithoutLogin(BaseTest):

    """
    Steps:
     * type url into browser without login
     * check landing page
    """

    @pytest.mark.usefixtures("setup")
    @pytest.mark.parametrize("url", params("testdata/app_url.json"))
    def test_access_without_login(self, url):
        self.navigate(url)
        assert f"You can only access '/{url}.html' when you are logged in." in self.login_page.error_text
