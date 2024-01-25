from .elements import Item
from constants.locators import InventoryPageLocators, ItemLocators
from pages.base_page import BasePage
from pages.details_page import DetailsPage
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
import logging


class SortBy:
    AZ = "az"
    ZA = "za"
    LOHI = "lohi"
    HILO = "hilo"


class InventoryItem(Item):
    image_locator = InventoryPageLocators.ITEM_IMG

    def __init__(self, container, driver, wait):
        self.logger = logging.getLogger(InventoryItem.__name__)
        self.driver = driver
        self.wait = wait
        super().__init__(container)

        image = container.find_element(*self.image_locator)
        self.image_link_locator = (
            By.ID,
            image.find_element(By.XPATH, "..").get_attribute("id"),
        )
        title = container.find_element(*ItemLocators.ITEM_TITLE)
        self.title_link_locator = (
            By.ID,
            title.find_element(By.XPATH, "..").get_attribute("id"),
        )

        data_test = container.find_element(*InventoryPageLocators.ADD_BUTTON).get_attribute("data-test")
        self.add_button_locator = (By.XPATH, f"//button[@data-test='{data_test}']")

        data_test = data_test.replace("add-to-cart", "remove")
        self.remove_button_locator = (By.XPATH, f"//button[@data-test='{data_test}']")

    def click_image(self):
        self.logger.info(f"click {self.title}'s image")
        image_link = self.wait.until(ec.presence_of_element_located(self.image_link_locator))
        image_link.click()
        return DetailsPage(self.driver, self.wait)

    def click_add(self):
        self.logger.info(f"add {self.title} to cart")
        button = self.wait.until(ec.presence_of_element_located(self.add_button_locator))
        button.click()

    def added(self):
        try:
            self.wait.until(ec.presence_of_element_located(self.remove_button_locator))
            return True
        except NoSuchElementException:
            return False

    def click_remove(self):
        self.logger.info(f"remove {self.title} from cart")
        button = self.wait.until(ec.presence_of_element_located(self.remove_button_locator))
        button.click()

    def click_title(self):
        self.logger.info(f"click {self.title}'s title")
        title = self.wait.until(ec.presence_of_element_located(self.title_link_locator))
        title.click()
        return DetailsPage(self.driver, self.wait)


class InventoryPage(BasePage):
    TITLE = "Products"

    def __init__(self, driver, wait):
        super().__init__(driver, wait)
        elements = wait.until(ec.presence_of_all_elements_located(InventoryPageLocators.ITEM))
        self.items = [InventoryItem(elem, driver, wait) for elem in elements]

    def __getitem__(self, key):
        return self.items[key]

    def get_items(self) -> list[InventoryItem]:
        return self.items

    def add_item(self, key):
        return self.items[key].click_add()

    def get_selected_items(self):
        return [i for i in self.items if i.added()]

    def add_all_items(self):
        for item in self.items:
            item.click_add()

    def sort(self, by: SortBy):
        sort = self.wait.until(ec.presence_of_element_located(InventoryPageLocators.SORT))
        sort.click()
        option = self.wait.until(ec.presence_of_element_located((By.XPATH, f'//option[@value="{str(by)}"]')))
        option.click()
