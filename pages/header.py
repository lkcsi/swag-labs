from pages.locators import HeaderLocators


class Cart(object):

    def __init__(self, driver):
        self.driver = driver

    def counter(self):
        badges = self.driver.find_elements(*HeaderLocators.CART_BADGE)
        if len(badges) == 0:
            return 0
        return int(badges[0].text)
