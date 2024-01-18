import logging
from selenium.common.exceptions import NoSuchElementException
from pages import (
    LoginPage,
    DetailsPage,
    InventoryPage,
    CheckoutTwoPage,
    CompletePage,
    CheckoutOnePage,
    CartPage,
    Cart,
    Burger,
)
from pages.locators import HeaderLocators
from selenium import webdriver


class SauceDemo(webdriver.Chrome):
    def __init__(self):
        super().__init__()
        self.get(self.PAGE_URL)
        self.implicitly_wait(0.5)
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)
        self.login_page = LoginPage(self)
        self.inventory_page = InventoryPage(self)
        self.cart_page = CartPage(self)
        self.checkout_one_page = CheckoutOnePage(self)
        self.details_page = DetailsPage(self)
        self.checkout_two_page = CheckoutTwoPage(self)
        self.complete_page = CompletePage(self)
        self.cart = Cart(self)
        self.burger = Burger(self)

    def logged_in(self) -> bool:
        try:
            self.find_element(*HeaderLocators.BURGER)
        except NoSuchElementException:
            return False
        return True

