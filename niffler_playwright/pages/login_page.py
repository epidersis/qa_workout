class LoginPage:
    def __init__(self, page):
        self.page = page

        self.username = page.locator("#username")
        self.password = page.locator("#password")
        self.submit = page.locator("#login-button")
        self.message = page.locator("#spendings")

    def locate_success(self):
        self.message = self.page.locator("#spendings")

    def locate_fail(self):
        self.message = self.page.locator(".form__error")

    def open(self, url):
        self.page.goto(url)

    def login(self, user, pwd, method):
        self.username.fill(user)
        self.password.fill(pwd)
        if method == 'click':
            self.submit.click()
        elif method == 'enter':
            self.password.press('Enter')
