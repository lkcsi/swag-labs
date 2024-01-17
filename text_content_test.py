from base_test import BaseTestCase
from parameterized.parameterized import parameterized_class
from database.database import users
from selenium.webdriver.common.by import By
import unittest
import re


@parameterized_class(users())
class TextContentTestCase(BaseTestCase):
    FUNCTION_PATTERN = r"\w+\.\w+\(\w*\)"

    def test_inventory_should_not_contain_functions(self):
        self.login()
        self.__page_should_not_contain_functions()

    def test_cart_should_not_contain_functions(self):
        self.login()
        self.add_all_items()
        self.click_cart()
        self.__page_should_not_contain_functions()

    def test_checkout_one_should_not_contain_functions(self):
        self.login()
        self.add_all_items()
        self.click_cart()
        self.click_checkout()
        self.__page_should_not_contain_functions()

    def test_checkout_two_should_not_contain_functions(self):
        self.login()
        self.add_all_items()
        self.click_cart()
        self.click_checkout()
        self.fill_billing_info()
        self.continue_to_step_two()
        self.__page_should_not_contain_functions()

    def __page_should_not_contain_functions(self):
        text = self.driver.find_element(By.XPATH, "/html/body").text
        text = text.split("\n")
        line_matches = []
        for line in text:
            matches = re.findall(self.FUNCTION_PATTERN, line)
            line_matches.append((line, matches))
        if line_matches:
            self.__print_matches(line_matches)

    def __print_matches(self, line_matches: [list]):
        for line in line_matches:
            if line[1]:
                self.logger.warning(f"In {line[0]} function name(s) found: {line[1]}")
        self.fail("Page should not contain functions")


if __name__ == "__main__":
    unittest.main()
