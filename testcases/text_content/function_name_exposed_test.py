from selenium.webdriver.common.by import By
import pytest
import re
from testcases import BaseTest


class TestTextContent(BaseTest):
    FUNCTION_PATTERN = r"\w+\.\w+\(\w*\)"

    @pytest.mark.usefixtures("setup")
    def test_inventory_functions_exposed(self):
        self.login()
        self.check_page()

    @pytest.mark.usefixtures("setup")
    def test_cart_functions_exposed(self):
        self.go_to_cart(add_all=True)
        self.check_page()

    @pytest.mark.usefixtures("setup")
    def test_checkout_one_functions_exposed(self):
        self.go_to_checkout_one(add_all=True)
        self.check_page()

    @pytest.mark.usefixtures("setup")
    def test_checkout_two_functions_exposed(self):
        self.go_to_checkout_two(add_all=True)
        self.check_page()

    def check_page(self):
        text = self.driver.find_element(By.XPATH, "/html/body").text
        matches = re.findall(self.FUNCTION_PATTERN, text)
        assert matches == []
