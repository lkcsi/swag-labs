from base import BaseTest
import pytest


class TestMissingCredentials(BaseTest):

    @pytest.mark.usefixtures("setup")
    def test_username_is_required(self):
        self.username = ""
        self.login()

        assert "Username is required" in self.login_page.error_text

    @pytest.mark.usefixtures("setup")
    def test_password_is_required(self):
        self.password = ""
        self.login()

        assert "Password is required" in self.login_page.error_text
