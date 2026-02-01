import pytest
from selene import browser
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope='session')
def browser_window_size():
    return 720, 540


# пусть будет один браузер на всю сессию 😶‍🌫️
@pytest.fixture(scope='session')
def driver(browser_window_size):
    x, y = browser_window_size
    options = Options()
    options.add_argument(f"--window-size={x},{y}")

    browser.config.driver_options = options
    browser.config.timeout = 10

    yield browser

    browser.quit()


@pytest.fixture(scope="session")
def base_url():
    return "https://duckduckgo.com/"
