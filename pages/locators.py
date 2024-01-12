from selenium.webdriver.common.by import By

class LoginPageLocators(object):
    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    SUBMIT = (By.ID, "login-button")
    ERROR = (By.CLASS_NAME, 'error-message-container')

class InventoryPageLocators(object):
    ITEM_LIST = (By.CLASS_NAME, 'inventory_list')
    ITEM = (By.CLASS_NAME, 'inventory_item')
    ITEM_IMG = (By.CLASS_NAME, 'inventory_item_img')
    ITEM_TITLE = (By.CLASS_NAME, 'inventory_item_name')