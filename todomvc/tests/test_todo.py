from selene import browser, have, be


def test_addition():
    browser.open('/')
    todo_input_field = browser.element('.new-todo').should(be.blank)
    todo_input_field.type('walk a dog').press_enter()
    todo_input_field.type('eat a donut').press_enter()
    todo_input_field.type('talk with guests').press_enter()

    browser.all('.todo-list>li').with_(timeout=browser.config.timeout * 2).should(have.size(3))
