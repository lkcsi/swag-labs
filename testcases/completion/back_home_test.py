import pytest

from base import BaseTest
from utilities import params_from_json as params
from pages import InventoryPage


class TestCompletion(BaseTest):

    @pytest.mark.usefixtures("setup")
    def test_back_home(self):
        complete_page = self.go_to_finish(add_all=True)
        complete_page.back_to_home()

        assert InventoryPage.TITLE == self.header.get_title(), "landed wrong page after completion"
        assert self.header.cart.counter() == 0, "selected items are not 0 after completion"
