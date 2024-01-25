from selenium.webdriver.common.by import By
import pytest
import re
from testcases import BaseTest

FUNCTION_PATTERN = r"\w+\.\w+\(\w*\)"


class TestFunctionNameExposed(BaseTest):

    """
    Steps:
     * login to app
     * navigate to tested page with url
     * check exposed functions in page content
    """

    @pytest.mark.usefixtures("setup")
    def test_inventory_function_name_exposed(self):
        self.login()
        self.check_page()

    @pytest.mark.usefixtures("setup")
    def test_cart_function_name_exposed(self):
        self.go_to_cart(add_all=True)
        self.check_page()

    @pytest.mark.usefixtures("setup")
    def test_checkout_one_function_name_exposed(self):
        self.go_to_checkout_one(add_all=True)
        self.check_page()

    @pytest.mark.usefixtures("setup")
    def test_checkout_two_function_name_exposed(self):
        self.go_to_checkout_two(add_all=True)
        self.check_page()

    def check_page(self):
        text = self.driver.find_element(By.XPATH, "/html/body").text
        matches = re.findall(FUNCTION_PATTERN, text)
        assert matches == []
