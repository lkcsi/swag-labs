from pages.locators import HeaderLocators


class Cart(object):
    def __init__(self, driver):
        self.driver = driver

    def counter(self):
        badges = self.driver.find_elements(*HeaderLocators.CART_BADGE)
        if len(badges) == 0:
            return 0
        return int(badges[0].text)

    def click(self):
        cart = self.driver.find_element(*HeaderLocators.CART_LINK)
        cart.click()


class SecondaryHeader(object):
    def __init__(self, driver):
        self.driver = driver

    def title(self):
        container = self.driver.find_element(*HeaderLocators.SEC_SECONDARY_CONTAINER)
        header = container.find_element(*HeaderLocators.TITLE)
        return header.text
