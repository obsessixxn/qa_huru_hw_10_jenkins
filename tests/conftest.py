import pytest
from selene import browser


@pytest.fixture(scope='session')
def in_browser():
    browser.driver.set_window_size(1920, 1080)