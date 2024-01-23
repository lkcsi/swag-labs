import logging

from base.locators import HeaderLocators
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
import pages


class Burger(object):

    def __init__(self, driver):
        self.driver = driver

    def click(self):
        self.driver.find_element(*HeaderLocators.BURGER).click()

    def click_logout(self):
        self.driver.find_element(*HeaderLocators.LOGOUT).click()


class Cart(object):
    def __init__(self, driver):
        self.driver = driver

    def counter(self):
        badges = self.driver.find_elements(*HeaderLocators.CART_BADGE)
        if len(badges) == 0:
            return 0
        return int(badges[0].text)

    def click(self):
        cart = self.driver.find_element(*HeaderLocators.CART_LINK)
        try:
            cart.click()
        except ElementClickInterceptedException:
            self.driver.execute_script("arguments[0].click();", cart)


class Header(object):

    def __init__(self, driver):
        self.driver = driver
        self.burger = Burger(driver)
        self.cart = Cart(driver)
        self.logger = logging.getLogger(Header.__name__)

    def get_title(self):
        try:
            container = self.driver.find_element(*HeaderLocators.SECONDARY_CONTAINER)
            header = container.find_element(*HeaderLocators.TITLE)
            return header.text
        except NoSuchElementException:
            return ""

    def click_cart(self):
        self.logger.info("click cart icon")
        self.cart.click()
        return pages.CartPage(self.driver)

    def logout(self):
        self.logger.info("click burger menu")
        self.burger.click()
        self.logger.info("click logout")
        self.burger.click_logout()

