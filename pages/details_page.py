from pages.locators import DetailsPageLocators
from pages.element import ImageItem
from utilities import file_logger


class DetailsItem(ImageItem):

    logger = file_logger()
    title_locator = DetailsPageLocators.ITEM_TITLE
    desc_locator = DetailsPageLocators.ITEM_DESC
    price_locator = DetailsPageLocators.ITEM_PRICE
    image_locator = DetailsPageLocators.ITEM_IMG

    def __init__(self, driver):
        self.driver = driver
        container = self.driver.find_element(*DetailsPageLocators.CONTAINER)
        super().__init__(container)

    def click_add(self):
        self.logger.info(f"from details page, add item {self.title} to cart")
        container = self.driver.find_element(*DetailsPageLocators.CONTAINER)
        button = container.find_element(*DetailsPageLocators.ADD_BUTTON)
        button.click()

    def click_remove(self):
        self.logger.info(f"from details page, remove item {self.title} from cart")
        container = self.driver.find_element(*DetailsPageLocators.CONTAINER)
        button = container.find_element(*DetailsPageLocators.ADD_BUTTON)
        button.click()


class DetailsPage(object):
    def __init__(self, driver):
        self.driver = driver

    def item(self):
        return DetailsItem(self.driver)

    def add_item(self):
        DetailsItem(self.driver).click_add()

