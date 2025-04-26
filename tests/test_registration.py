# tests/test_registration.py

import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *
from helpers import perform_registration

@pytest.mark.usefixtures("browser")
class TestRegistration:

    # Тест успешной регистрации
    def test_successful_registration(self, browser):
        browser.get(MAIN_PAGE_URL)
        browser.find_element(*REGISTER_BUTTON_MAIN_PAGE).click()
        wait = WebDriverWait(browser, 10)
        wait.until(EC.visibility_of_element_located(REGISTRATION_FORM_NAME_INPUT))
        unique_email = f"test+{int(time.time())}@example.com"
        perform_registration(browser, 'Иван Иванов', unique_email, 'ValidPassw0rd!')
        wait.until(EC.visibility_of_element_located(PERSONAL_ACCOUNT_LINK))
        personal_account_text = browser.find_element(*PERSONAL_ACCOUNT_LINK).text
        assert personal_account_text == 'Личный кабинет'

    # Тест ошибки при вводе короткого пароля
    def test_short_password_error(self, browser):
        browser.get(MAIN_PAGE_URL)
        browser.find_element(*REGISTER_BUTTON_MAIN_PAGE).click()
        wait = WebDriverWait(browser, 10)
        wait.until(EC.visibility_of_element_located(REGISTRATION_FORM_NAME_INPUT))
        unique_email = f"test+{int(time.time())}@example.com"
        perform_registration(browser, 'Иван Иванов', unique_email, 'short')
        error_message = browser.find_element(*ERROR_MESSAGE).text
        assert "Минимальная длина пароля — 6 символов" in error_message

    # Тест на ошибку при вводе неправильного адреса электронной почты
    def test_invalid_email_format(self, browser):
        browser.get(MAIN_PAGE_URL)
        browser.find_element(*REGISTER_BUTTON_MAIN_PAGE).click()
        wait = WebDriverWait(browser, 10)
        wait.until(EC.visibility_of_element_located(REGISTRATION_FORM_NAME_INPUT))
        self.perform_registration(browser, 'Иван Иванов', 'invalid_email', 'ValidPassw0rd!')
        error_message = browser.find_element_by_class_name('error-message').text
        self.assertIn('Некорректный адрес электронной почты', error_message)

    # Тест на недопустимость пустого имени
    def test_empty_name_field(self, browser):
        browser.get(MAIN_PAGE_URL)
        browser.find_element(*REGISTER_BUTTON_MAIN_PAGE).click()
        wait = WebDriverWait(browser, 10)
        wait.until(EC.visibility_of_element_located(REGISTRATION_FORM_NAME_INPUT))
        unique_email = f"test+{int(time.time())}@example.com"
        self.perform_registration(browser, '', unique_email, 'ValidPassw0rd!')
        error_message = browser.find_element_by_class_name('error-message').text
        self.assertIn('Необходимо заполнить поле Имя', error_message)
