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

    def __init__(self, elem):
        self.elem = elem
        super().__init__(elem)

    def click_image(self):
        image = self.elem.find_element(*InventoryPageLocators.ITEM_IMG)
        image.click()

    def click_add(self):
        button = self.elem.find_element(*InventoryPageLocators.ADD_BUTTON)
        button.click()

    def click_remove(self):
        button = self.elem.find_element(*InventoryPageLocators.ADD_BUTTON)
        button.click()

    def click_title(self):
        title = self.elem.find_element(*ItemLocators.ITEM_TITLE)
        title.click()


class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.items = [InventoryItem(i) for i in driver.find_elements(*InventoryPageLocators.ITEM)]

    def sort(self, by: SortBy):
        sort = self.driver.find_element(*InventoryPageLocators.SORT)
        sort.click()
        locator = f'//option[@value="{str(by)}"]'
        option = WebDriverWait(self.driver, 3).until(
            lambda d: d.find_element(By.XPATH, locator)
        )
        option.click()
