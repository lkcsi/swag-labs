import pytest
from testcases import BaseTest


class TestTimeout(BaseTest):

    """
    Steps:
     * login to app
     * trigger timeout by remove cookies
     * refresh page
     * check error message
    """

    @pytest.mark.usefixtures("setup")
    def test_refresh_after_timeout(self):
        self.go_to_inventory()
        self.trigger_timeout()
        assert "You can only access '/inventory.html' when you are logged in." in self.login_page.error_text

    def trigger_timeout(self):
        self.driver.delete_cookie("session-username")
        self.driver.refresh()
