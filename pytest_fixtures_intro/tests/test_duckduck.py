import pytest
from selene import browser, have


@pytest.mark.parametrize(
    'search_query, search_result',
    [
        ('Куда уходит лето?', 'Ядвига Поплавская'),
        ('Собака', 'Породы собак от А до Я')
    ]
)
def test_selene_duckduck_search(driver, base_url, search_query, search_result):
    browser.open(base_url)
    search_field = browser.element('#searchbox_input')
    search_field.type(search_query).press_enter()

    search_results = browser.element('#web_content_wrapper')
    search_results.should(have.text(search_result))
