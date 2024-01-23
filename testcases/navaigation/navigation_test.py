import pytest
from pages.inventory_page import InventoryPage
from base import BaseTest
from utilities import params_from_json as params


class TestNavigation(BaseTest):

    @pytest.mark.usefixtures("setup")
    @pytest.mark.parametrize("url,page", params("testdata/direct_access_urls.json"))
    def test_should_access_with_login(self, url, page):
        self.login()
        self.driver.get(f"{self.base_url}/{url}.html")
        assert self.login_page.error_text == "", f"should navigate to {page} when logged in"

    @pytest.mark.usefixtures("setup")
    @pytest.mark.parametrize("url", params("testdata/no_direct_access_urls.json"))
    def test_should_not_access_without_checkout(self, url):
        self.login()
        self.driver.get(f"{self.base_url}/{url}.html")
        assert self.header.get_title() == InventoryPage.TITLE, f"page {url} should not access directly"

    @pytest.mark.usefixtures("setup")
    @pytest.mark.parametrize("url", params("testdata/app_url.json"))
    def test_should_not_access_without_login(self, url):
        self.driver.get(f"{self.base_url}/{url}.html")
        assert f"You can only access '/{url}.html' when you are logged in." in self.login_page.error_text
