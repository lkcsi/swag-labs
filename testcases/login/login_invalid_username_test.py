from testcases import BaseTest
import pytest
from utilities import params_from_json as params


class TestInvalidUsernameTest(BaseTest):

    @pytest.mark.usefixtures("setup")
    @pytest.mark.parametrize("username,password", params("testdata/invalid_usernames.json"))
    def test_login_invalid_username(self, username, password):

        self.username = username
        self.password = password
        self.login()

        assert (
                "Username and password do not match any user in this service"
                in self.login_page.error_text
        )
