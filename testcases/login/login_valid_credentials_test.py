from pages import InventoryPage
from testcases import BaseTest
import pytest
from utilities import params_from_json as params


class TestLoginValidCredentials(BaseTest):
    @pytest.mark.usefixtures("setup")
    @pytest.mark.parametrize("username,password", params("testdata/valid_credentials.json"))
    def test_login_valid_credentials(self, username, password):
        self.username = username
        self.password = password
        self.login()
        assert InventoryPage.TITLE == self.header.get_title()
