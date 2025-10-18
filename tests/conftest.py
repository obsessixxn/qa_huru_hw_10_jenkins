import pytest
from selene import browser


@pytest.fixture(scope='session')
def setup_firefox():
    browser.config.driver_name = 'firefox'
    browser.driver.set_window_size(1920, 1080)