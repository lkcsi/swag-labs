from .elements import QuantityItem, BaseElement, TextElement
from constants.locators import ItemLocators, CheckoutPageTwoLocators
from pages.base_page import BasePage
from pages.inventory_page import InventoryPage
from pages.complete_page import CompletePage
from selenium.common.exceptions import TimeoutException
import logging
from selenium.webdriver.support import expected_conditions as ec


class OverviewItem(QuantityItem):
    quantity_locator = CheckoutPageTwoLocators.QUANTITY

    def __init__(self, key, driver):
        self.key = key
        self.driver = driver
        container = driver.find_elements(*CheckoutPageTwoLocators.ITEM)[key]
        super().__init__(container)

    def click_title(self):
        elem = self.driver.find_elements(*CheckoutPageTwoLocators.ITEM)[self.key]
        title = elem.find_element(*ItemLocators.ITEM_TITLE)
        title.click()


class Total(TextElement):
    locator = CheckoutPageTwoLocators.TOTAL


class Subtotal(TextElement):
    locator = CheckoutPageTwoLocators.SUBTOTAL


class FinishButton(BaseElement):
    locator = CheckoutPageTwoLocators.FINISH


class CancelButton(BaseElement):
    locator = CheckoutPageTwoLocators.CANCEL


class CheckoutTwoPage(BasePage):
    TITLE = "Checkout: Overview"
    total = Total()
    subtotal = Subtotal()
    finish_button = FinishButton()
    cancel_button = CancelButton()

    def __init__(self, driver, wait):
        super().__init__(driver, wait)
        self.logger = logging.getLogger(CheckoutTwoPage.__name__)

    def finish(self):
        self.logger.info("click finish button")
        self.finish_button.click()
        return CompletePage(self.driver, self.wait)

    def cancel(self):
        self.logger.info("click cancel button")
        self.cancel_button.click()
        return InventoryPage(self.driver, self.wait)

    def get_items(self):
        driver = self.driver
        wait = self.wait
        try:
            elements = wait.until(ec.presence_of_all_elements_located(CheckoutPageTwoLocators.ITEM))
        except TimeoutException:
            elements = []
        return [OverviewItem(i, driver) for i in range(len(elements))]
