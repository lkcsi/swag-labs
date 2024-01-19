from base import ItemLocators, CheckoutPageTwoLocators, QuantityItem, TextElement, BaseElement
from utilities import file_logger
import pages


class OverviewItem(QuantityItem):
    quantity_locator = CheckoutPageTwoLocators.QUANTITY

    def __init__(self, driver, key):
        self.key = key
        self.driver = driver
        elem = driver.find_elements(*CheckoutPageTwoLocators.ITEM)[key]
        super().__init__(elem)

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


class CheckoutTwoPage:
    TITLE = "Checkout: Overview"
    total = Total()
    subtotal = Subtotal()
    finish_button = FinishButton()
    cancel_button = CancelButton()
    logger = file_logger()

    def __init__(self, driver):
        self.driver = driver

    def finish(self):
        self.logger.info("click finish button")
        self.finish_button.click()
        return pages.CompletePage(self.driver)

    def cancel(self):
        self.logger.info("click cancel button")
        self.cancel_button.click()
        return pages.InventoryPage(self.driver)

    def get_items(self):
        driver = self.driver
        size = len(driver.find_elements(*CheckoutPageTwoLocators.ITEM))
        return [OverviewItem(driver, i) for i in range(size)]
