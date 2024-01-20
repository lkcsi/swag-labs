import os.path

from selenium import webdriver
from pages import LoginPage
from base import Header
import pytest
import os
import uuid
import pytest_html
from pytest_html import extras
from utilities import save_image

PAGE_URL = "https://www.saucedemo.com"


@pytest.fixture(scope="function")
def setup(request, browser):
    if browser == "firefox":
        driver = webdriver.Firefox()
    else:
        driver = webdriver.Chrome()
    driver.get(PAGE_URL)
    driver.fullscreen_window()
    driver.implicitly_wait(0.5)
    request.cls.driver = driver
    request.cls.login_page = LoginPage(driver)
    request.cls.header = Header(driver)
    yield
    driver.close()


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture(scope="class", autouse=True)
def browser(request):
    return request.config.getoption("--browser")


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    extra_html = getattr(report, "extras", [])

    if report.when == "call":
        page_url = pytest_html.extras.url(PAGE_URL)
        extra_html.append(page_url)

        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail) and item.config.option.htmlpath:
            image = pytest_html.extras.html(save_image(item))
            extra_html.append(image)

        report.extras = extra_html


def pytest_html_report_title(report):
    report.title = "My Title"
