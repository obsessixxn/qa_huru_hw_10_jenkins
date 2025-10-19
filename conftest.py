import tempfile

import pytest
from selene import Config, Browser
from selenium import webdriver
from utils import attach


@pytest.fixture(scope='session')
def in_browser():
    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=1920,1080")

    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "128.0",
        "selenoid:options": {
            "enableVideo": True,
            "enableVNS": True
        }
    }

    options.capabilities.update(selenoid_capabilities)
    driver = webdriver.Remote(
        command_executor="https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=options)

    browser = Browser(
        Config(
            driver=driver,
        )
    )

    yield browser

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)

    browser.quit()
