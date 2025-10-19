import tempfile

import pytest
from selene import Config, Browser
from selenium import webdriver


@pytest.fixture(scope='session')
def in_browser():
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")
    # options.add_argument("--no-sandbox")
    # options.add_argument("--disable-dev-shm-usage")
    # options.add_argument("--disable-gpu")
    # options.add_argument("--window-size=1920,1080")

    options.add_argument(f"--user-data-dir={tempfile.mkdtemp()}")

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
            base_url="https://demoqa.com",
            timeout=6,
            window_width=1920,
            window_height=1080,
        )
    )

    yield browser

    browser.quit()
