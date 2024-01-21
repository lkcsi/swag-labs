from selenium import webdriver
from pages import LoginPage
from base import Header
import pytest
import pytest_html
from pytest_html import extras
from utilities import save_image
from dotenv import load_dotenv
import os

@pytest.fixture(scope="function")
def setup(request, browser, sauce_user):

    load_dotenv()
    request.cls.password = os.getenv("PASSWORD")
    username = os.getenv("SAUCE_USER")
    if sauce_user:
        username = sauce_user
    url = os.getenv("BASE_URL")

    driver = get_driver(browser)
    driver.get(url)
    driver.fullscreen_window()
    driver.implicitly_wait(0.5)
    request.cls.driver = driver
    request.cls.login_page = LoginPage(driver)
    request.cls.header = Header(driver)
    request.cls.base_url = url
    request.cls.username = username
    yield
    driver.close()


def get_driver(browser):
    if browser == "firefox":
        return webdriver.Firefox()
    else:
        return webdriver.Chrome()

def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--sauce-user")


@pytest.fixture(scope="class", autouse=True)
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="class", autouse=True)
def sauce_user(request):
    return request.config.getoption("--sauce-user")


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    extra_html = getattr(report, "extras", [])

    if report.when == "call":
        page_url = pytest_html.extras.url(item.cls.base_url)
        extra_html.append(page_url)

        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail) and item.config.option.htmlpath:
            image = pytest_html.extras.html(save_image(item))
            extra_html.append(image)

        report.extras = extra_html


def pytest_html_report_title(report):
    report.title = "My Title"
