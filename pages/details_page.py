from base.locators import DetailsPageLocators
from base.element import ImageItem, BaseElement
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


class BackButton(BaseElement):
    locator = DetailsPageLocators.BACK


class DetailsPage(object):
    logger = file_logger()
    back = BackButton()

    def __init__(self, driver):
        self.driver = driver

    def get_item(self):
        return DetailsItem(self.driver)

    def add_item(self):
        DetailsItem(self.driver).click_add()

    def remove_item(self):
        DetailsItem(self.driver).click_remove()

    def back_to_products(self):
        self.logger.info("click back to products")
        self.back.click()
