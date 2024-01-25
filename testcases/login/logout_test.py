import pytest
from testcases import BaseTest


class TestLogout(BaseTest):

    @pytest.mark.usefixtures("setup")
    def test_logout(self):
        self.login()
        self.header.logout()

        assert self.header.get_title() == ""
