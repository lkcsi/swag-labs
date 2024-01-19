import pytest
from pages import LoginPage
from base import Header, BaseTest
from utilities import params_from_json as params
from base import BaseTest


class TestLogout(BaseTest):

    @pytest.mark.usefixtures("setup")
    @pytest.mark.parametrize("username,password", params("testdata/valid_credentials.json"))
    def test_logout(self, username, password):
        login = LoginPage(self.driver)
        login.login(username, password)

        header = Header(self.driver)
        header.logout()
