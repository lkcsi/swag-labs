import pytest
from pages.inventory_page import InventoryPage
from testcases import BaseTest
from utilities import params_from_json as params


class TestAccessUrlWithoutCheckout(BaseTest):

    """
    Steps:
     * login to app
     * type checkout page url
     * check landing page
    """

    @pytest.mark.usefixtures("setup")
    @pytest.mark.parametrize("url", params("testdata/no_direct_access_urls.json"))
    def test_access_without_checkout(self, url):
        self.login()
        self.navigate(url)
        assert self.header.get_title() == InventoryPage.TITLE, f"page {url} should not be accessed directly"

