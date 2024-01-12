from selenium.webdriver.common.by import By

class LoginPageLocators(object):
    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    SUBMIT = (By.ID, "login-button")
    ERROR = (By.CLASS_NAME, 'error-message-container')