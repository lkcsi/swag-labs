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
    ADD_BUTTON = (By.CLASS_NAME, "btn_inventory")
    SORT = (By.CLASS_NAME, "product_sort_container")


class ItemLocators(object):
    ITEM_TITLE = (By.CLASS_NAME, "inventory_item_name")
    ITEM_DESC = (By.CLASS_NAME, "inventory_item_desc")
    ITEM_PRICE = (By.CLASS_NAME, "inventory_item_price")


class CartPageLocators(object):
    CONTAINER = (By.ID, "cart_content_container")
    ITEM = (By.CLASS_NAME, "cart_item")
    CART_QTY = (By.CLASS_NAME, "cart_quantity")
    REMOVE_BUTTON = (By.CLASS_NAME, "cart_button")
    CHECKOUT_BUTTON = (By.XPATH, "//button[@data-test='checkout']")
    CONTINUE_BUTTON = (By.XPATH, "//button[@data-test='continue-shopping']")


class HeaderLocators(object):
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    SECONDARY_CONTAINER = (By.CLASS_NAME, "header_secondary_container")
    TITLE = (By.CLASS_NAME, "title")
    BURGER = (By.XPATH, "//button[@id='react-burger-menu-btn']")
    LOGOUT = (By.XPATH, "//a[@id='logout_sidebar_link']")


class DetailsPageLocators(object):
    ITEM_TITLE = (By.CLASS_NAME, "inventory_details_name")
    CONTAINER = (By.CLASS_NAME, "inventory_item_container")
    ITEM_DESC = (By.CLASS_NAME, "inventory_details_desc")
    ITEM_PRICE = (By.CLASS_NAME, "inventory_details_price")
    ITEM_IMG = (By.TAG_NAME, "img")
    ADD_BUTTON = (By.CLASS_NAME, "btn_inventory")
    BACK = (By.XPATH, "//button[@data-test='back-to-products']")


class CheckoutPageOneLocators(object):
    CONTAINER = (By.CLASS_NAME, "checkout_info_wrapper")
    FIRST_NAME = (By.XPATH, "//input[@data-test='firstName']")
    LAST_NAME = (By.XPATH, "//input[@data-test='lastName']")
    POSTAL_CODE = (By.XPATH, "//input[@data-test='postalCode']")
    CONTINUE = (By.XPATH, "//input[@data-test='continue']")
    CANCEL = (By.XPATH, "//button[@data-test='cancel']")
    ERROR = (By.XPATH, "//h3[@data-test='error']")


class CheckoutPageTwoLocators(object):
    ITEM = (By.CLASS_NAME, "cart_item")
    QUANTITY = (By.CLASS_NAME, "cart_quantity")
    SUBTOTAL = (By.CLASS_NAME, "summary_subtotal_label")
    TOTAL = (By.CLASS_NAME, "summary_total_label")
    FINISH = (By.XPATH, "//button[@data-test='finish']")
    CANCEL = (By.XPATH, "//button[@data-test='cancel']")


class CompletePageLocators(object):
    FINISH_BUTTON = (By.XPATH, "//button[@data-test='back-to-products']")
