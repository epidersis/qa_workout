import pytest
from selene import browser
from selenium import webdriver


@pytest.fixture(scope='session', autouse=True)
def browser_setup():  # noqa
    browser.config.base_url = 'https://todomvc.com/examples/emberjs/todomvc/dist/'
    browser.config.timeout = 2.0
    driver_options = webdriver.ChromeOptions()
    driver_options.add_argument('--headless=new')
    browser.config.driver_options = driver_options
    yield
    browser.quit()
