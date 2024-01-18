from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 3)

    def wait_until_element_found(self, locator: tuple[str, str]):
        return self.wait.until(ec.presence_of_element_located(locator))
