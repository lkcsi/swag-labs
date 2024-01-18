from pages.locators import HeaderLocators
from utilities import file_logger


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
        cart.click()


class SecondaryHeader(object):
    logger = file_logger()

    def __init__(self, driver):
        self.driver = driver
        self.burger = Burger(driver)
        self.cart = Cart(driver)

    def get_title(self):
        container = self.driver.find_element(*HeaderLocators.SEC_SECONDARY_CONTAINER)
        header = container.find_element(*HeaderLocators.TITLE)
        return header.text

    def click_cart(self):
        self.logger.info("click cart icon")
        self.cart.click()

    def logout(self):
        self.logger.info("click burger menu")
        self.burger.click()
        self.logger.info("click logout")
        self.burger.click_logout()

