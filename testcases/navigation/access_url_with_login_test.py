import pytest
from pages.inventory_page import InventoryPage
from testcases import BaseTest
from utilities import params_from_json as params


class TestAccessUrlWithLogin(BaseTest):

    """
    Steps:
     * login to app
     * type url into browser
     * check landing page
    """

    @pytest.mark.usefixtures("setup")
    @pytest.mark.parametrize("url,page", params("testdata/direct_access_urls.json"))
    def test_access_url_with_login(self, url, page):
        self.login()
        self.navigate(url)
        assert self.login_page.error_text == "", f"should navigate to {page} when logged in"
