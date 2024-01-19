import os.path

from selenium import webdriver
from pages import LoginPage
from base import Header
import pytest
import pytest_html
from pytest_html import extras

PAGE_URL = "https://www.saucedemo.com"


@pytest.fixture(scope="function")
def setup(request, browser):
    if browser == "firefox":
        driver = webdriver.Firefox()
    else:
        driver = webdriver.Chrome()
    driver.get(PAGE_URL)
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
    driver = item.cls.driver
    if report.when == "call":
        # always add url to report
        extra_html.append(pytest_html.extras.url(PAGE_URL))
        xfail = hasattr(report, "wasxfail")
        html_path = item.config.option.htmlpath
        if (report.skipped and xfail) or (report.failed and not xfail) and html_path:
            report_dir = os.path.dirname(html_path)
            file_name = report.nodeid.replace("::", "_") + ".png"
            driver.save_screenshot(os.path.join(report_dir, file_name))
            # only add additional html on failure
            html = ("<div><img src='%s' alt='screenshot' style='width:300px;height:200px'"
                    "onclick='window.open(this.src)' align='right'/><div>")
            extra_html.append(pytest_html.extras.html(html))
        report.extras = extra_html


def pytest_html_report_title(report):
    report.title = "My Title"
