from selenium.webdriver.common.by import By


class LoginPageLocators(object):
    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    SUBMIT = (By.ID, "login-button")
    ERROR = (By.CLASS_NAME, "error-message-container")


class InventoryPageLocators(object):
    ITEM_LIST = (By.CLASS_NAME, "inventory_list")
    ITEM = (By.CLASS_NAME, "inventory_item")
    ITEM_IMG = (By.TAG_NAME, "img")
    ITEM_TITLE = (By.CLASS_NAME, "inventory_item_name")
    ITEM_DESC = (By.CLASS_NAME, "inventory_item_desc")
    ITEM_PRICE = (By.CLASS_NAME, "inventory_item_price")
    ADD_BUTTON = (By.CLASS_NAME, "btn_inventory")
    SORT = (By.CLASS_NAME, "product_sort_container")


class HeaderLocators(object):
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")


class DetailsPageLocators(object):
    ITEM_TITLE = (By.CLASS_NAME, "inventory_details_name")
    CONTAINER = (By.CLASS_NAME, "inventory_item_container")
    ITEM_DESC = (By.CLASS_NAME, "inventory_details_desc")
    ITEM_PRICE = (By.CLASS_NAME, "inventory_details_price")
    ITEM_IMG = (By.TAG_NAME, "img")
    ADD_BUTTON = (By.CLASS_NAME, "btn_inventory")
