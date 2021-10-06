from .base_page import BasePage
import allure


class MailPage(BasePage):
    get_number_letters = "[title='«Simbirsoft Тестовое задание»']"
    click_on_write_letter = "[class='mail-ComposeButton-Text']"
    enter_address = "//span[text()='Кому']/ancestor::label/following-sibling::div[" \
                    "@class='compose-LabelRow-Content']//div[@is='x-bubbles'] "
    enter_topic_name = "//input[@name='subject']"
    enter_message_text = "//div[@role='presentation']//div[@placeholder='Напишите что-нибудь']"
    click_on_send_email = "//div[@class='ComposeControlPanel-Part']//button[@class='Button2 Button2_pin_circle-circle " \
                          "Button2_view_default Button2_size_l'] "
    verification_email_sent = "//span[text()='Письмо отправлено']"

    @allure.step("Получить количество писем")
    def number_of_identical_topics(self):
        letters = self.browser.find_elements_by_css_selector(self.get_number_letters)
        return len(letters)

    @allure.step("Кликнуть на кнопку 'написать письмо'")
    def click_write_letter_button(self):
        self.browser.find_element_by_css_selector(self.click_on_write_letter).click()

    @allure.step("Ввести адрес получателя")
    def send_keys_address(self, my_mail):
        self.browser.find_element_by_xpath(self.enter_address).send_keys(my_mail)

    @allure.step("Ввести название темы")
    def send_keys_title(self, title):
        self.browser.find_element_by_xpath(self.enter_topic_name).send_keys(title)

    @allure.step("Ввести текст сообщения")
    def send_keys_massage(self, massage):
        self.browser.find_element_by_xpath(self.enter_message_text).send_keys(massage)

    @allure.step("Кликнуть на кнопку 'отправить письмо'")
    def click_send_letter_button(self):
        self.browser.find_element_by_xpath(self.click_on_send_email).click()

    @allure.step("Проверить отправку письма")
    def check_send_letter_page(self, text):
        exp_text = self.browser.find_element_by_xpath(self.verification_email_sent).text
        assert exp_text == text
