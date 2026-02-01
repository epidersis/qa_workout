import allure
import pytest
from selene import be, browser


def test_check_on_qa_workout_pull_requests(driver, base_url):
    with allure.step('Находим репозиторий'):
        browser.open(base_url)
        browser.element('a[data-tab-item="repositories"]').click()
        browser.element('#your-repos-filter').type('qa_workout')
        # тут бы, конечно, заставить его подождать фильтрации результатов
        # но суть не в selene
        browser.element('a[href="/epidersis/qa_workout"]').click()

    with allure.step('Открываем пулл реквесты'):
        browser.element('span[data-content="Pull requests"]').click()

    with allure.step('Смотрим закрытые'):
        browser.element('a[data-ga-click="Pull Requests, Table state, Closed"]').should(be.visible).click()

    with allure.step('Проверяем, что список таких реквестов не пустой'):
        browser.element('div[aria-label="Issues"]').should(be.not_.blank)
