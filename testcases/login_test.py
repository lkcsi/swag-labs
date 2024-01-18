from pages import InventoryPage
import pytest
from utilities import params_from_json as params


class TestValidParameters:
    @pytest.mark.usefixtures("setup", "login_page", "header")
    @pytest.mark.parametrize(
        "username,password", params("../testdata/valid_credentials.json")
    )
    def test_login_with_valid_credentials(self, username, password):
        self.login_page.login(username, password)
        assert InventoryPage.TITLE == self.header.get_title()


class TestWrongParameters:
    @pytest.mark.usefixtures("setup", "login_page")
    @pytest.mark.parametrize(
        "username,password", params("../testdata/invalid_credentials.json")
    )
    def test_wrong_password(self, username, password):
        self.login_page.login(username, password)

        assert (
            "Username and password do not match any user in this service"
            in self.login_page.error_text
        )


class TestMissingParameters:
    @pytest.mark.usefixtures("setup", "login_page")
    def test_username_is_required(self):
        self.login_page.login("", "secret_sauce")

        assert "Username is required" in self.login_page.error_text

    @pytest.mark.usefixtures("setup", "login_page")
    def test_password_is_required(self):
        self.login_page.login("standard_user", "")

        assert "Password is required" in self.login_page.error_text
