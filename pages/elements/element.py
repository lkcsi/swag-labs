from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as ec


class BaseElement(object):
    locator = None

    def __get__(self, obj, owner):
        wait = obj.wait
        return wait.until(ec.presence_of_element_located(self.locator))


class ValueElement(BaseElement):
    def __set__(self, obj, value):
        wait = obj.wait
        element = wait.until(ec.presence_of_element_located(self.locator))
        element.clear()
        element.send_keys(value)

    def __get__(self, obj, owner):
        wait = obj.wait
        element = wait.until(ec.presence_of_element_located(self.locator))
        return element.get_attribute("value")


class TextElement(BaseElement):
    def __get__(self, obj, owner):
        wait = obj.wait
        try:
            element = wait.until(ec.presence_of_element_located(self.locator))
            return element.text
        except TimeoutException:
            return ""


