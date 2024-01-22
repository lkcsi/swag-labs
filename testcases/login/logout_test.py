import pytest
from utilities import params_from_json as params
from base import BaseTest


class TestLogout(BaseTest):

    @pytest.mark.usefixtures("setup")
    def test_logout(self):
        self.login()
        self.header.logout()

        assert self.header.get_title() == ""
