import pytest
from selene import be


def test_check_on_qa_workout_pull_requests(driver, base_url):
    driver.open(base_url)
    driver.element('a[data-tab-item="repositories"]').click()
    driver.element('#your-repos-filter').type('qa_workout')
    # тут бы, конечно, заставить его подождать фильтрации результатов
    # но суть не в selene
    driver.element('a[href="/epidersis/qa_workout"]').click()
    driver.element('span[data-content="Pull requests"]').click()
    driver.element('a[data-ga-click="Pull Requests, Table state, Closed"]').should(be.visible).click()
    driver.element('div[aria-label="Issues"]').should(be.not_.blank)
