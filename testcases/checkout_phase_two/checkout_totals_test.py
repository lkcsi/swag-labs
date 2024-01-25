import pytest

from testcases import BaseTest
from utilities import convert_price_tag_to_float as convert_to_float
from utilities import sum_price_of_items as price_sum

TAX = 1.08


class TestCheckoutTotals(BaseTest):

    @pytest.mark.usefixtures("setup")
    def test_checkout_totals(self):
        inventory_page = self.login()
        inventory_page.add_all_items()
        items_to_buy = inventory_page.get_items()

        cart_page = self.header.click_cart()
        checkout_one_page = cart_page.checkout()
        checkout_two_page = checkout_one_page.fill_and_continue()

        expected = price_sum(items_to_buy)
        actual = checkout_two_page.subtotal
        actual = convert_to_float(actual)

        assert expected == actual, f"subtotal is not equals: {expected}"

        expected = expected * TAX
        expected = round(expected, 2)
        actual = checkout_two_page.total
        actual = convert_to_float(actual)

        assert expected == actual, f"subtotal is not equals: {expected}"

