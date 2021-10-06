from src.pages.auth_page import AuthPage
from src.pages.mail_page import MailPage
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from src.resources.auth_data import mail_login, mail_password
import allure

browser = webdriver.Remote(
    command_executor="http://localhost:4444/wd/hub",
    desired_capabilities=DesiredCapabilities.CHROME)


@allure.story("Отправить письмо на собственную почту")
def test():
    my_mail = mail_login
    password = mail_password
    title = "«Simbirsoft Тестовое задание.<Назаров>»"
    link = "https://mail.yandex.ru"

    auth_page = AuthPage(browser)
    mail_page = MailPage(browser)
    browser.get(link)

    auth_page.click_on_enter_button()
    auth_page.input_email(my_mail)
    auth_page.enter_email()
    auth_page.input_password(password)
    auth_page.enter_password()

    letters = mail_page.number_of_identical_topics()
    mail_page.click_write_letter_button()
    mail_page.send_keys_address(my_mail)
    mail_page.send_keys_title(title)
    mail_page.send_keys_massage(letters)
    mail_page.click_send_letter_button()
    mail_page.check_send_letter_page("Письмо отправлено")

    browser.quit()
