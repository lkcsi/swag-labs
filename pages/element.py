from selenium.webdriver.support.ui import WebDriverWait

class ValueElement(object):
    def __set__(self, obj, value):
        driver = obj.driver
        element = driver.find_element(*self.locator)
        element.clear()
        element.send_keys(value)

    def __get__(self, obj, owner):
        driver = obj.driver
        element = driver.find_element(*self.locator)
        return element.get_attribute("value")
        
class TextElement(object):
    def __get__(self, obj, owner):
        driver = obj.driver
        element = driver.find_element(*self.locator)
        return element.text

class ListElement(object):
    def __get__(self, obj, owner):
        driver = obj.driver
        return driver.find_elements(*self.locator)