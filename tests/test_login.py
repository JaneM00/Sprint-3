# tests/test_login.py

import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *
from helpers import perform_login

@pytest.mark.usefixtures("browser")
class TestLogin:

    # Тест входа по кнопке «Войти в аккаунт» на главной
    def test_login_via_main_page_button(self, browser):
        browser.get(MAIN_PAGE_URL)
        browser.find_element(*LOGIN_BUTTON_MAIN_PAGE).click()
        wait = WebDriverWait(browser, 10)
        wait.until(EC.visibility_of_element_located(LOGIN_FORM_EMAIL_INPUT))
        perform_login(browser, 'existing_user@example.com', 'valid_password')
        wait.until(EC.visibility_of_element_located(PERSONAL_ACCOUNT_LINK))
        personal_account_text = browser.find_element(*PERSONAL_ACCOUNT_LINK).text
        assert personal_account_text == 'Личный кабинет'

    # Тест входа через кнопку «Личный кабинет»
    def test_login_via_personal_account_link(self, browser):
        browser.get(MAIN_PAGE_URL)
        browser.find_element(*PERSONAL_ACCOUNT_LINK).click()
        wait = WebDriverWait(browser, 10)
        wait.until(EC.visibility_of_element_located(LOGIN_FORM_EMAIL_INPUT))
        perform_login(browser, 'existing_user@example.com', 'valid_password')
        wait.until(EC.visibility_of_element_located(PERSONAL_ACCOUNT_LINK))
        personal_account_text = browser.find_element(*PERSONAL_ACCOUNT_LINK).text
        assert personal_account_text == 'Личный кабинет'

    # Тест входа через кнопку в форме регистрации
    def test_login_via_register_form(self, browser):
        browser.get(MAIN_PAGE_URL)
        browser.find_element(*REGISTER_BUTTON_MAIN_PAGE).click()
        wait = WebDriverWait(browser, 10)
        wait.until(EC.visibility_of_element_located(LOGIN_FORM_EMAIL_INPUT))
        self.perform_login(browser, 'existing_user@example.com', 'valid_password')
        wait.until(EC.visibility_of_element_located(PERSONAL_ACCOUNT_LINK))
        personal_account_text = browser.find_element(*PERSONAL_ACCOUNT_LINK).text
        self.assertEqual(personal_account_text, 'Личный кабинет')

    # Тест входа через кнопку в форме восстановления пароля
    def test_login_via_reset_password_form(self, browser):
        browser.get(MAIN_PAGE_URL)
        browser.find_element(*FORGOT_PASSWORD_LINK).click()
        wait = WebDriverWait(browser, 10)
        wait.until(EC.visibility_of_element_located(LOGIN_FORM_EMAIL_INPUT))
        self.perform_login(browser, 'existing_user@example.com', 'valid_password')
        wait.until(EC.visibility_of_element_located(PERSONAL_ACCOUNT_LINK))
        personal_account_text = browser.find_element(*PERSONAL_ACCOUNT_LINK).text
        self.assertEqual(personal_account_text, 'Личный кабинет')
