from pages.locators import DetailsPageLocators


class DetailsItem(object):
    def __init__(self, driver):
        self.driver = driver

    def click_add(self):
        container = self.driver.find_element(*DetailsPageLocators.CONTAINER)
        button = container.find_element(*DetailsPageLocators.ADD_BUTTON)
        button.click()

    def __getitem__(self, key):
        container = self.driver.find_element(*DetailsPageLocators.CONTAINER)
        if key == 'title':
            return container.find_element(*DetailsPageLocators.ITEM_TITLE).text
        elif key == 'description':
            return container.find_element(*DetailsPageLocators.ITEM_DESC).text
        elif key == 'price':
            return container.find_element(*DetailsPageLocators.ITEM_PRICE).text
        elif key == 'image':
            image = container.find_element(*DetailsPageLocators.ITEM_IMG)
            return image.get_attribute('src').split("/")[-1]


class DetailsPage(object):

    def __init__(self, driver):
        self.item = DetailsItem(driver)
