import pytest
from selene import browser
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope='session')
def base_url():
    return 'https://github.com/epidersis'


@pytest.fixture
def driver():
    options = Options()
    browser.config.driver_options = options

    yield browser

    browser.quit()
