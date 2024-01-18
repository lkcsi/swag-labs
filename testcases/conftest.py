from selenium import webdriver
from pages import LoginPage, InventoryPage, CartPage, DetailsPage
from base import SecondaryHeader
import pytest
import json

PAGE_URL = "https://www.saucedemo.com"


@pytest.fixture(scope="function")
def setup(request):
    driver = webdriver.Chrome()
    driver.get(PAGE_URL)
    driver.implicitly_wait(0.5)
    request.cls.driver = driver
    yield
    driver.close()


@pytest.fixture(scope="function")
def login_page(request):
    driver = request.cls.driver
    request.cls.login_page = LoginPage(driver)


@pytest.fixture(scope="function")
def header(request):
    driver = request.cls.driver
    request.cls.header = SecondaryHeader(driver)


@pytest.fixture(scope="function")
def inventory_page(request):
    driver = request.cls.driver
    request.cls.inventory_page = InventoryPage(driver)


@pytest.fixture(scope="function")
def cart_page(request):
    driver = request.cls.driver
    request.cls.cart_page = CartPage(driver)


@pytest.fixture(scope="function")
def details_page(request):
    driver = request.cls.driver
    request.cls.details_page = DetailsPage(driver)
