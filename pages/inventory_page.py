from pages.locators import InventoryPageLocators, ItemLocators
from selenium.webdriver.support.ui import WebDriverWait
from pages.element import ImageItem
from selenium.webdriver.common.by import By


class SortBy:
    AZ = "az"
    ZA = "za"
    LOHI = "lohi"
    HILO = "hilo"


class InventoryItem(ImageItem):
    image_locator = InventoryPageLocators.ITEM_IMG

    def __init__(self, driver, key):
        self.key = key
        self.driver = driver
        elem = driver.find_elements(*InventoryPageLocators.ITEM)[key]
        super().__init__(elem)

    def click_image(self):
        elem = self.driver.find_elements(*InventoryPageLocators.ITEM)[self.key]
        image = elem.find_element(*InventoryPageLocators.ITEM_IMG)
        image.click()

    def click_add(self):
        elem = self.driver.find_elements(*InventoryPageLocators.ITEM)[self.key]
        button = elem.find_element(*InventoryPageLocators.ADD_BUTTON)
        button.click()

    def click_remove(self):
        elem = self.driver.find_elements(*InventoryPageLocators.ITEM)[self.key]
        button = elem.find_element(*InventoryPageLocators.ADD_BUTTON)
        button.click()

    def click_title(self):
        elem = self.driver.find_elements(*InventoryPageLocators.ITEM)[self.key]
        title = elem.find_element(*ItemLocators.ITEM_TITLE)
        title.click()


class InventoryPage:
    TITLE = "Products"

    def __init__(self, driver):
        self.driver = driver

    def get_items(self):
        driver = self.driver
        size = len(driver.find_elements(*InventoryPageLocators.ITEM))
        return [InventoryItem(driver, i) for i in range(size)]

    def sort(self, by: SortBy):
        sort = self.driver.find_element(*InventoryPageLocators.SORT)
        sort.click()
        option = WebDriverWait(self.driver, 3).until(
            lambda d: d.find_element(By.XPATH, f'//option[@value="{str(by)}"]')
        )
        option.click()
