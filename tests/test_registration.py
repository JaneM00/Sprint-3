# tests/test_registration.py

import time
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *

class TestRegistration(unittest.TestCase):

    def setUp(self):
        pass  # Всё управление браузером передано в фикстуру

    def tearDown(self):
        pass  # Всё управление браузером передано в фикстуру

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
        self.assertEqual(personal_account_text, 'Личный кабинет')

    # Тест ошибки при вводе короткого пароля
    def test_short_password_error(self, browser):
        browser.get(MAIN_PAGE_URL)
        browser.find_element(*REGISTER_BUTTON_MAIN_PAGE).click()
        wait = WebDriverWait(browser, 10)
        wait.until(EC.visibility_of_element_located(REGISTRATION_FORM_NAME_INPUT))
        unique_email = f"test+{int(time.time())}@example.com"
        browser.find_element(*REGISTRATION_FORM_NAME_INPUT).send_keys('Иван Иванов')
        browser.find_element(*REGISTRATION_FORM_EMAIL_INPUT).send_keys(unique_email)
        browser.find_element(*REGISTRATION_FORM_PASSWORD_INPUT).send_keys('12345')  # Недостаточно символов
        browser.find_element(*REGISTRATION_FORM_SUBMIT_BUTTON).click()
        error_message = browser.find_element_by_class_name('error-message').text
        self.assertIn('Пароль должен содержать минимум 6 символов', error_message)

    # Тест при вводе неправильного адреса электронной почты
    def test_invalid_email_error(self, browser):
        browser.get(MAIN_PAGE_URL)
        browser.find_element(*REGISTER_BUTTON_MAIN_PAGE).click()
        wait = WebDriverWait(browser, 10)
        wait.until(EC.visibility_of_element_located(REGISTRATION_FORM_NAME_INPUT))
        browser.find_element(*REGISTRATION_FORM_NAME_INPUT).send_keys('Иван Иванов')
        browser.find_element(*REGISTRATION_FORM_EMAIL_INPUT).send_keys('invalid_email')
        browser.find_element(*REGISTRATION_FORM_PASSWORD_INPUT).send_keys('ValidPassw0rd!')
        browser.find_element(*REGISTRATION_FORM_SUBMIT_BUTTON).click()
        error_message = browser.find_element_by_class_name('error-message').text
        self.assertIn('Некорректный адрес электронной почты', error_message)

    # Тест на недопустимость пустого имени
    def test_missing_name_error(self, browser):
        browser.get(MAIN_PAGE_URL)
        browser.find_element(*REGISTER_BUTTON_MAIN_PAGE).click()
        wait = WebDriverWait(browser, 10)
        wait.until(EC.visibility_of_element_located(REGISTRATION_FORM_NAME_INPUT))
        unique_email = f"test+{int(time.time())}@example.com"
        browser.find_element(*REGISTRATION_FORM_EMAIL_INPUT).send_keys(unique_email)
        browser.find_element(*REGISTRATION_FORM_PASSWORD_INPUT).send_keys('ValidPassw0rd!')
        browser.find_element(*REGISTRATION_FORM_SUBMIT_BUTTON).click()
        error_message = browser.find_element_by_class_name('error-message').text
        self.assertIn('Необходимо заполнить поле Имя', error_message)
