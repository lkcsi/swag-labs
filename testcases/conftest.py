from selenium import webdriver
from pages import LoginPage
from base import Header
import pytest
import pytest_html
from pytest_html import extras
from utilities import save_image
from dotenv import load_dotenv
import os
from configparser import ConfigParser


@pytest.fixture(scope="function")
def setup(request, driver, conf):

    load_dotenv()

    base_url = conf['BaseUrl']
    driver.get(base_url)
    driver.fullscreen_window()
    driver.implicitly_wait(float(conf['WaitTime']))

    request.cls.driver = driver
    request.cls.login_page = LoginPage(driver)
    request.cls.header = Header(driver)
    request.cls.base_url = base_url
    request.cls.username = conf['Username']
    request.cls.password = os.getenv("PASSWORD")
    yield
    driver.close()


@pytest.fixture()
def correct_env(request, conf):
    request.cls.correct_env_username = conf['CorrectEnvUsername']
    request.cls.correct_env_base_url = conf['CorrectEnvBaseUrl']


def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--env")


@pytest.fixture(scope="function", autouse=True)
def driver(request):
    browser = request.config.getoption("--browser")
    if browser == "firefox":
        return webdriver.Firefox()
    else:
        return webdriver.Chrome()


@pytest.fixture(scope="class", autouse=True)
def conf(request):
    env = request.config.getoption("--env")
    if not env:
        env = 'DEFAULT'
    config = ConfigParser()
    config.read('config.ini')
    return config[env]


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
    report.title = "SauceDemo Tests"
