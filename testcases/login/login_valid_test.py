from pages import InventoryPage
from base import BaseTest
import pytest


class TestValidParameters(BaseTest):
    @pytest.mark.usefixtures("setup")
    def test_login_with_valid_credentials(self):
        self.login()
        assert InventoryPage.TITLE == self.header.get_title()
