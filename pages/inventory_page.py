from pages.locators import InventoryPageLocators


class InventoryItem(object):
    def __init__(self, elem):
        self.elem = elem

    def get_map(self):
        return {
            'title': self.__getitem__('title'),
            'description': self.__getitem__('description'),
            'price': self.__getitem__('price'),
            'image': self.__getitem__('image')
        }

    def __getitem__(self, key):
        if key == 'title':
            return self.elem.find_element(*InventoryPageLocators.ITEM_TITLE).text
        elif key == 'description':
            return self.elem.find_element(*InventoryPageLocators.ITEM_DESC).text
        elif key == 'price':
            return self.elem.find_element(*InventoryPageLocators.ITEM_PRICE).text
        elif key == 'image':
            image = self.elem.find_element(*InventoryPageLocators.ITEM_IMG)
            return image.get_attribute('src').split("/")[-1]

    def click_image(self):
        image = self.elem.find_element(*InventoryPageLocators.ITEM_IMG)
        image.click()

    def click_add(self):
        button = self.elem.find_element(*InventoryPageLocators.ADD_BUTTON)
        button.click()

    def click_title(self):
        title = self.elem.find_element(*InventoryPageLocators.ITEM_TITLE)
        title.click()


class InventoryItems:

    def __init__(self, driver):
        self.driver = driver

    def __getitem__(self, key):
        driver = self.driver
        items = driver.find_elements(*InventoryPageLocators.ITEM)
        return InventoryItem(items[key])

    def __len__(self):
        driver = self.driver
        items = driver.find_elements(*InventoryPageLocators.ITEM)
        return len(items)


class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.items = InventoryItems(driver)