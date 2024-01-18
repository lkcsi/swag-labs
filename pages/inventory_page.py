from base.locators import InventoryPageLocators, ItemLocators
from selenium.webdriver.support.ui import WebDriverWait
from base.element import ImageItem
from selenium.webdriver.common.by import By
from utilities import file_logger
import pages


class SortBy:
    AZ = "az"
    ZA = "za"
    LOHI = "lohi"
    HILO = "hilo"


class InventoryItem(ImageItem):
    logger = file_logger()
    image_locator = InventoryPageLocators.ITEM_IMG

    def __init__(self, driver, elem):
        super().__init__(elem)
        self.driver = driver

        image = elem.find_element(*self.image_locator)
        self.image_link_locator = (
            By.ID,
            image.find_element(By.XPATH, "..").get_attribute("id"),
        )
        title = elem.find_element(*ItemLocators.ITEM_TITLE)
        self.title_link_locator = (
            By.ID,
            title.find_element(By.XPATH, "..").get_attribute("id"),
        )

        data_test = elem.find_element(*InventoryPageLocators.ADD_BUTTON).get_attribute(
            "data-test"
        )
        self.add_button_locator = (By.XPATH, f"//button[@data-test='{data_test}']")

        data_test = data_test.replace("add-to-cart", "remove")
        self.remove_button_locator = (By.XPATH, f"//button[@data-test='{data_test}']")

    def click_image(self):
        image_link = self.driver.find_element(*self.image_link_locator)
        image_link.click()
        return pages.DetailsPage(self.driver)

    def click_add(self):
        self.logger.info(f"add {self.title} to cart")
        button = self.driver.find_element(*self.add_button_locator)
        button.click()

    def click_remove(self):
        self.logger.info(f"remove {self.title} from cart")
        button = self.driver.find_element(*self.remove_button_locator)
        button.click()

    def click_title(self):
        title = self.driver.find_element(*self.title_link_locator)
        title.click()
        return pages.DetailsPage(self.driver)


class InventoryPage:
    TITLE = "Products"

    def __init__(self, driver):
        self.driver = driver

    def get_items(self) -> list[InventoryItem]:
        driver = self.driver
        elements = driver.find_elements(*InventoryPageLocators.ITEM)
        return [InventoryItem(driver, elem) for elem in elements]

    def add_item(self, key):
        element = self.driver.find_elements(*InventoryPageLocators.ITEM)[key]
        InventoryItem(self.driver, element).click_add()

    def add_all_items(self):
        for element in self.driver.find_elements(*InventoryPageLocators.ITEM):
            InventoryItem(self.driver, element).click_add()

    def sort(self, by: SortBy):
        sort = self.driver.find_element(*InventoryPageLocators.SORT)
        sort.click()
        option = WebDriverWait(self.driver, 3).until(
            lambda d: d.find_element(By.XPATH, f'//option[@value="{str(by)}"]')
        )
        option.click()
