# tests/test_registration.py

import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *  # Импортируем локаторы из отдельного файла

@pytest.fixture(scope='session')
def browser():
    """Фикстура для запуска и остановки браузера."""
    from selenium import webdriver
    driver = webdriver.Chrome()  # Используем Chrome, но можно выбрать любой подходящий драйвер
    yield driver
    driver.quit()

class TestRegistration:

    # Тест успешной регистрации
    def test_successful_registration(self, browser):
        browser.get(MAIN_PAGE_URL)
        browser.find_element(*REGISTER_BUTTON_MAIN_PAGE).click()
        wait = WebDriverWait(browser, 10)
        wait.until(EC.visibility_of_element_located(REGISTRATION_FORM_NAME_INPUT))
        unique_email = f"test+{int(time.time())}@example.com"
        browser.find_element(*REGISTRATION_FORM_NAME_INPUT).send_keys('Иван Иванов')
        browser.find_element(*REGISTRATION_FORM_EMAIL_INPUT).send_keys(unique_email)
        browser.find_element(*REGISTRATION_FORM_PASSWORD_INPUT).send_keys('ValidPassw0rd!')
        browser.find_element(*REGISTRATION_FORM_SUBMIT_BUTTON).click()
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
        browser.find_element(*REGISTRATION_FORM_NAME_INPUT).send_keys('Иван Иванов')
        browser.find_element(*REGISTRATION_FORM_EMAIL_INPUT).send_keys(unique_email)
        browser.find_element(*REGISTRATION_FORM_PASSWORD_INPUT).send_keys('12345')  # Пароль слишком короткий
        browser.find_element(*REGISTRATION_FORM_SUBMIT_BUTTON).click()
        error_message = browser.find_element(*ERROR_MESSAGE_ELEMENT).text
        assert 'Пароль должен содержать минимум 6 символов' in error_message

    # Тест при вводе некорректного email
    def test_invalid_email_error(self, browser):
        browser.get(MAIN_PAGE_URL)
        browser.find_element(*REGISTER_BUTTON_MAIN_PAGE).click()
        wait = WebDriverWait(browser, 10)
        wait.until(EC.visibility_of_element_located(REGISTRATION_FORM_NAME_INPUT))
        browser.find_element(*REGISTRATION_FORM_NAME_INPUT).send_keys('Иван Иванов')
        browser.find_element(*REGISTRATION_FORM_EMAIL_INPUT).send_keys('invalid_email')
        browser.find_element(*REGISTRATION_FORM_PASSWORD_INPUT).send_keys('ValidPassw0rd!')
        browser.find_element(*REGISTRATION_FORM_SUBMIT_BUTTON).click()
        error_message = browser.find_element(*ERROR_MESSAGE_ELEMENT).text
        assert 'Некорректный адрес электронной почты' in error_message

    # Тест на ошибку при отсутствии имени
    def test_missing_name_error(self, browser):
        browser.get(MAIN_PAGE_URL)
        browser.find_element(*REGISTER_BUTTON_MAIN_PAGE).click()
        wait = WebDriverWait(browser, 10)
        wait.until(EC.visibility_of_element_located(REGISTRATION_FORM_NAME_INPUT))
        unique_email = f"test+{int(time.time())}@example.com"
        browser.find_element(*REGISTRATION_FORM_EMAIL_INPUT).send_keys(unique_email)
        browser.find_element(*REGISTRATION_FORM_PASSWORD_INPUT).send_keys('ValidPassw0rd!')
        browser.find_element(*REGISTRATION_FORM_SUBMIT_BUTTON).click()
        error_message = browser.find_element(*ERROR_MESSAGE_ELEMENT).text
        assert 'Необходимо заполнить поле Имя' in error_message
