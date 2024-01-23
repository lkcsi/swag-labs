import pytest
from base import BaseTest


class TestTimeout(BaseTest):

    @pytest.mark.usefixtures("setup")
    def test_refresh_after_timeout(self):
        self.go_to_inventory()
        self.driver.delete_cookie("session-username")
        self.driver.refresh()

        assert "You can only access '/inventory.html' when you are logged in." in self.login_page.error_text
