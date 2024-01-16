from pages.locators import ItemLocators, OverviewPageLocators
from pages.element import QuantityItem, TextElement, BaseElement


class OverviewItem(QuantityItem):
    quantity_locator = OverviewPageLocators.QUANTITY

    def __init__(self, driver, key):
        self.key = key
        self.driver = driver
        elem = driver.find_elements(*OverviewPageLocators.ITEM)[key]
        super().__init__(elem)

    def click_title(self):
        elem = self.driver.find_elements(*OverviewPageLocators.ITEM)[self.key]
        title = elem.find_element(*ItemLocators.ITEM_TITLE)
        title.click()


class Total(TextElement):
    locator = OverviewPageLocators.TOTAL


class Subtotal(TextElement):
    locator = OverviewPageLocators.SUBTOTAL


class FinishButton(BaseElement):
    locator = OverviewPageLocators.FINISH


class CancelButton(BaseElement):
    locator = OverviewPageLocators.CANCEL


class OverviewPage:
    TITLE = "Checkout: Overview"
    total = Total()
    subtotal = Subtotal()
    finish_button = FinishButton()
    cancel_button = CancelButton()

    def __init__(self, driver):
        self.driver = driver

    def get_items(self):
        driver = self.driver
        size = len(driver.find_elements(*OverviewPageLocators.ITEM))
        return [OverviewItem(driver, i) for i in range(size)]
