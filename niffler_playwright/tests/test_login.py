import os
import pytest
from playwright.sync_api import expect
from pages.login_page import LoginPage


@pytest.mark.parametrize(
    "username,password,expected_text",
    [
        ("stas", "12345", "History of Spendings"),
    ]
)
def test_login_success_click(page, base_url, username, password, expected_text):
    # url = "file:///" + os.path.abspath("index.html")
    login_page = LoginPage(page)
    login_page.locate_success()
    login_page.open(base_url)
    login_page.login(username, password, 'click')

    expect(login_page.message).to_contain_text(expected_text)


@pytest.mark.parametrize(
    "username,password,expected_text",
    [
        ("stas", "12345", "History of Spendings"),
    ]
)
def test_login_success_enter(page, base_url, username, password, expected_text):
    # url = "file:///" + os.path.abspath("index.html")
    login_page = LoginPage(page)
    login_page.locate_success()
    login_page.open(base_url)
    login_page.login(username, password, 'enter')

    expect(login_page.message).to_contain_text(expected_text)


@pytest.mark.parametrize(
    "username,password,expected_text",
    [
        ("admin", "qwerty1234", "Неверные учетные данные пользователя"),
    ]
)
def test_login_fail(page, base_url, username, password, expected_text):
    # url = "file:///" + os.path.abspath("index.html")
    login_page = LoginPage(page)
    login_page.locate_fail()
    login_page.open(base_url)
    login_page.login(username, password, 'click')

    expect(login_page.message).to_contain_text(expected_text)
