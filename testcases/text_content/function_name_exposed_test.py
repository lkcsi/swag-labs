from selenium.webdriver.common.by import By
import pytest
import re
from utilities import params_from_json as params
from base import BaseTest


class TestTextContent(BaseTest):
    FUNCTION_PATTERN = r"\w+\.\w+\(\w*\)"

    @pytest.mark.usefixtures("setup")
    def test_inventory_functions_exposed(self):
        self.login()
        self.check_page()

    @pytest.mark.usefixtures("setup")
    def test_cart_functions_exposed(self):
        inventory_page = self.login()
        inventory_page.add_all_items()
        self.header.click_cart()
        self.check_page()

    @pytest.mark.usefixtures("setup")
    def test_checkout_one_functions_exposed(self):
        inventory_page = self.login()
        inventory_page.add_all_items()
        cart_page = self.header.click_cart()
        cart_page.checkout()
        self.check_page()

    @pytest.mark.usefixtures("setup")
    def test_checkout_two_functions_exposed(self):
        inventory_page = self.login()
        inventory_page.add_all_items()
        cart_page = self.header.click_cart()
        checkout_one = cart_page.checkout()
        checkout_one.fill_and_continue()
        self.check_page()

    def check_page(self):
        text = self.driver.find_element(By.XPATH, "/html/body").text
        matches = re.findall(self.FUNCTION_PATTERN, text)
        assert matches == []