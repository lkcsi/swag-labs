from selenium import webdriver
from pages import LoginPage
from base import Header
import pytest

PAGE_URL = "https://www.saucedemo.com"


@pytest.fixture(scope="function")
def driver(request, browser):
    if browser == "firefox":
        driver = webdriver.Firefox()
    else:
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
    request.cls.header = Header(driver)


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture(scope="class", autouse=True)
def browser(request):
    return request.config.getoption("--browser")
#
#
# @pytest.fixture(scope="function")
# def inventory_page(request):
#     driver = request.cls.driver
#     request.cls.inventory_page = InventoryPage(driver)
#
#
# @pytest.fixture(scope="function")
# def cart_page(request):
#     driver = request.cls.driver
#     request.cls.cart_page = CartPage(driver)
#
#
# @pytest.fixture(scope="function")
# def details_page(request):
#     driver = request.cls.driver
#     request.cls.details_page = DetailsPage(driver)
#
#
# @pytest.fixture(scope="function")
# def checkout_one_page(request):
#     driver = request.cls.driver
#     request.cls.checkout_one_page = CheckoutOnePage(driver)
#
#
# @pytest.fixture(scope="function")
# def checkout_two_page(request):
#     driver = request.cls.driver
#     request.cls.checkout_two_page = CheckoutTwoPage(driver)
