from .base_page import BasePage
import allure

class AuthPage(BasePage):
    click_on_the_entrance = "//a[contains(@class, 'HeadBanner-Button-Enter')]"
    enter_login = "[name= 'login']"
    login_after_login = "[type = 'submit']"
    enter_password = "passp-field-passwd"
    login_after_password = "[type = 'submit']"

    @allure.step("Кликнуть на кнопку входа")
    def click_on_enter_button(self):
        self.browser.find_element_by_xpath(self.click_on_the_entrance).click()

    @allure.step("Ввести логин")
    def input_email(self, my_mail):
        self.browser.find_element_by_css_selector(self.enter_login).send_keys(my_mail)

    @allure.step("Кликнуть на кнопку входа")
    def enter_email(self):
        self.browser.find_element_by_css_selector(self.login_after_login).click()

    @allure.step("Ввести пароль")
    def input_password(self, password):
        self.browser.find_element_by_id(self.enter_password).send_keys(password)

    @allure.step("Кликнуть на кнопку входа")
    def enter_password(self):
        self.browser.find_element_by_css_selector(self.login_after_password).click()
