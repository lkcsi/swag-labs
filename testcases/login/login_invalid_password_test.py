from base import BaseTest
import pytest
from utilities import params_from_json as params


class TestInvalidPassword(BaseTest):

    @pytest.mark.usefixtures("setup")
    @pytest.mark.parametrize("username,password", params("testdata/invalid_passwords.json"))
    def test_wrong_password(self, username, password):
        self.username = username
        self.password = password
        self.login()

        assert (
                "Username and password do not match any user in this service"
                in self.login_page.error_text
        )
