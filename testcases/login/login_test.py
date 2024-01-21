from pages import InventoryPage
from base import BaseTest
import pytest
from utilities import params_from_json as params


class TestValidParameters(BaseTest):
    @pytest.mark.usefixtures("setup")
    def test_login_with_valid_credentials(self):
        self.login()
        assert InventoryPage.TITLE == self.header.get_title()

    @pytest.mark.usefixtures("setup")
    def test_wrong_password(self):
        self.login()

        assert (
                "Username and password do not match any user in this service"
                in self.login_page.error_text
        )

    @pytest.mark.usefixtures("setup")
    def test_username_is_required(self):
        self.login_page.login("", "secret_sauce")

        assert "Username is required" in self.login_page.error_text

    @pytest.mark.usefixtures("setup", "login_page")
    def test_password_is_required(self):
        self.login_page.login("standard_user", "")

        assert "Password is required" in self.login_page.error_text
