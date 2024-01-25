import logging

from constants import HeaderLocators
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, TimeoutException
import pages
from selenium.webdriver.support import expected_conditions as ec


class Burger(object):

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def click(self):
        self.wait.until(ec.presence_of_element_located(HeaderLocators.BURGER)).click()

    def click_logout(self):
        self.wait.until(ec.presence_of_element_located(HeaderLocators.LOGOUT)).click()


class Cart(object):
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def counter(self):
        try:
            badge = self.wait.until(ec.presence_of_element_located(HeaderLocators.CART_BADGE))
            return int(badge.text)
        except TimeoutException:
            return 0

    def click(self):
        cart = self.wait.until(ec.presence_of_element_located(HeaderLocators.CART_LINK))
        try:
            cart.click()
        except ElementClickInterceptedException:
            self.driver.execute_script("arguments[0].click();", cart)


class Header(object):

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        self.burger = Burger(driver, wait)
        self.cart = Cart(driver, wait)
        self.logger = logging.getLogger(Header.__name__)

    def get_title(self):
        try:
            container = self.wait.until(ec.presence_of_element_located(HeaderLocators.SECONDARY_CONTAINER))
            header = container.find_element(*HeaderLocators.TITLE)
            return header.text
        except NoSuchElementException:
            return ""
        except TimeoutException:
            return ""

    def click_cart(self):
        self.logger.info("click cart icon")
        self.cart.click()
        return pages.CartPage(self.driver, self.wait)

    def logout(self):
        self.logger.info("click burger menu")
        self.burger.click()
        self.logger.info("click logout")
        self.burger.click_logout()

