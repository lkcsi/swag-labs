from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException
from parameterized import parameterized_class
from selenium import webdriver
from database.database import users
import unittest

from base_test import BaseTestCase


@parameterized_class(users())
class LoginTestCase(BaseTestCase):

    def test_login(self):
        self.login()

    def test_wrong_password(self):
        login = self.login_page
        login.username_input = self.username
        login.password_input = "invalid"
        login.click_submit()

        self.assertTrue(
            "Username and password do not match any user in this service"
            in login.error_text,
            "Login should fail with invalid credentials",
        )


class MissingParameters(BaseTestCase):

    def test_username_is_required(self):
        self.login_page.password_input = "test"
        self.login_page.click_submit()
        self.assertTrue("Username is required" in self.login_page.error_text)

    def test_password_is_required(self):
        self.login_page.username_input = "test"
        self.login_page.click_submit()
        self.assertTrue("Password is required" in self.login_page.error_text)


if __name__ == "__main__":
    unittest.main()
