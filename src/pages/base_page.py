class BasePage:
    def __init__(self, browser):
        self.browser = browser
        self.browser.implicitly_wait(30)
