class BasePage(object):

    BASE_URL = "https://www.saucedemo.com"

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
