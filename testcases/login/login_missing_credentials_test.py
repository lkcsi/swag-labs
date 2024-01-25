from testcases import BaseTest
import pytest


class TestMissingCredentials(BaseTest):

    """
    Steps:
     * navigate to login page
     * type missing password / username
     * click submit button
     * check error text
    """

    @pytest.mark.usefixtures("setup")
    def test_login_missing_username(self):
        self.username = ""
        self.login()

        assert "Username is required" in self.login_page.error_text

    @pytest.mark.usefixtures("setup")
    def test_login_missing_password(self):
        self.password = ""
        self.login()

        assert "Password is required" in self.login_page.error_text
