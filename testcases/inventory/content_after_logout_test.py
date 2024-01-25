from testcases import BaseTest
import pytest


class TestContentAfterLogout(BaseTest):

    @pytest.mark.usefixtures("setup")
    def test_content_after_logout(self):
        inventory = self.go_to_inventory()
        inventory.add_all_items()
        expected_items = inventory.get_items()
        self.logout()

        inventory = self.go_to_inventory()
        assert inventory.get_items() == expected_items

