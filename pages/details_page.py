import logging

from constants.locators import DetailsPageLocators
from pages.elements import BaseElement, Item
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as ec


class DetailsItem(Item):

    title_locator = DetailsPageLocators.ITEM_TITLE
    desc_locator = DetailsPageLocators.ITEM_DESC
    price_locator = DetailsPageLocators.ITEM_PRICE

    def __init__(self, driver, wait):
        container = wait.until(ec.presence_of_element_located(DetailsPageLocators.CONTAINER))
        super().__init__(container)
        self.driver = driver
        self.wait = wait
        self.logger = logging.getLogger(DetailsItem.__name__)

    def click_add(self):
        self.logger.info(f"from details page, add item {self.title} to cart")
        container = self.wait.until(ec.presence_of_element_located(DetailsPageLocators.CONTAINER))
        button = container.find_element(*DetailsPageLocators.ADD_BUTTON)
        button.click()

    def click_remove(self):
        self.logger.info(f"from details page, remove item {self.title} from cart")
        container = self.wait.until(ec.presence_of_element_located(DetailsPageLocators.CONTAINER))
        button = container.find_element(*DetailsPageLocators.ADD_BUTTON)
        button.click()


class BackButton(BaseElement):
    locator = DetailsPageLocators.BACK


class DetailsPage(BasePage):
    back = BackButton()

    def __init__(self, driver, wait):
        super().__init__(driver, wait)
        self.logger = logging.getLogger(DetailsPage.__name__)

    def get_item(self):
        return DetailsItem(self.driver, self.wait)

    def add_item(self):
        DetailsItem(self.driver, self.wait).click_add()

    def remove_item(self):
        DetailsItem(self.driver, self.wait).click_remove()

    def back_to_products(self):
        self.logger.info("click back to products")
        self.back.click()
