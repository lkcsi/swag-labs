import unittest
import logging
from pages.login_page import LoginPage
from selenium import webdriver


class BaseTestCase(unittest.TestCase):
    logger = logging.getLogger()
    username = ""
    password = ""
    error = False

    def setUp(self):
        self.logger.setLevel(logging.INFO)
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.saucedemo.com")
        self.error = False

    def login(self):
        login_page = LoginPage(self.driver)
        if not login_page.login(self.username, self.password):
            self.fail("timeout")

    def tearDown(self):
        self.driver.close()
