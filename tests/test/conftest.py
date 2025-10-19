import tempfile

import pytest
from selene import browser, Config
from selenium import webdriver


@pytest.fixture(scope='session')
def in_browser():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")

    options.add_argument(f"--user-data-dir={tempfile.mkdtemp()}")

    driver = webdriver.Chrome(options=options)

    browser.config = Config(
        driver=driver,
        base_url="https://demoqa.com",
        timeout=6,
        window_width=1920,
        window_height=1080,
    )

    yield browser

    browser.quit()
