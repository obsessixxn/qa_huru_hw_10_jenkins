import pytest
from selene import browser
from selenium import webdriver


@pytest.fixture(scope='session')
def in_browser():
    options = webdriver.ChromeOptions()
    browser.config.driver_name = 'chrome'
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.config.base_url = 'https://demoqa.com'
    browser.config.timeout = 10
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    yield browser
