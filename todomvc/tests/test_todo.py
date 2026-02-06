import time

from selene import browser, have, be
import pytest


def test_addition():
    browser.open('/')
    todo_input_field = browser.element('.new-todo').should(be.blank)

    todos = [
        'walk a dog',
        'eat a donut',
        'talk with guests',
    ]

    for todo in todos:
        todo_input_field.type(todo).press_enter()

    browser.all('.todo-list>li').with_(timeout=browser.config.timeout * 2).should(have.size(3))


def test_check():
    browser.open('/')

    for i in range(1, 4):
        browser.element(f'.todo-list>li:nth-child({i})').element('.toggle').click()
        browser.element(f'.todo-list>li:nth-child({i})').should(have.css_class('completed'))
