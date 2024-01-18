import pytest
import unittest
from pages import LoginPage
from base import SecondaryHeader
from utilities import params_from_json as params


class TestLogout:

    @pytest.mark.usefixtures("setup")
    @pytest.mark.parametrize("username,password", params("../testdata/valid_credentials.json"))
    def test_logout(self, username, password):
        login = LoginPage(self.driver)
        login.login(username, password)

        header = SecondaryHeader(self.driver)
        header.logout()


if __name__ == "__main__":
    unittest.main()
