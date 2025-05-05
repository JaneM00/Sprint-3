# tests/test_login.py

import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *

@pytest.fixture(scope='session')
def browser():
    """Инициализируем и возвращаем экземпляр браузера."""
    from selenium import webdriver
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

class TestLogin:

    # Тест входа по кнопке «Войти в аккаунт» на главной странице
    def test_login_via_main_page_button(self, browser):
        browser.get(MAIN_PAGE_URL)
        browser.find_element(*LOGIN_BUTTON_MAIN_PAGE).click()
        wait = WebDriverWait(browser, 10)
        wait.until(EC.visibility_of_element_located(LOGIN_FORM_EMAIL_INPUT))
        browser.find_element(*LOGIN_FORM_EMAIL_INPUT).send_keys('existing_user@example.com')
        browser.find_element(*LOGIN_FORM_PASSWORD_INPUT).send_keys('valid_password')
        browser.find_element(*LOGIN_FORM_SUBMIT_BUTTON).click()
        wait.until(EC.visibility_of_element_located(PERSONAL_ACCOUNT_LINK))
        personal_account_text = browser.find_element(*PERSONAL_ACCOUNT_LINK).text
        assert personal_account_text == 'Личный кабинет'

    # Тест входа через ссылку «Личный кабинет»
    def test_login_via_personal_account_link(self, browser):
        browser.get(MAIN_PAGE_URL)
        browser.find_element(*PERSONAL_ACCOUNT_LINK).click()
        wait = WebDriverWait(browser, 10)
        wait.until(EC.visibility_of_element_located(LOGIN_FORM_EMAIL_INPUT))
        browser.find_element(*LOGIN_FORM_EMAIL_INPUT).send_keys('existing_user@example.com')
        browser.find_element(*LOGIN_FORM_PASSWORD_INPUT).send_keys('valid_password')
        browser.find_element(*LOGIN_FORM_SUBMIT_BUTTON).click()
        wait.until(EC.visibility_of_element_located(PERSONAL_ACCOUNT_LINK))
        personal_account_text = browser.find_element(*PERSONAL_ACCOUNT_LINK).text
        assert personal_account_text == 'Личный кабинет'

    # Тест входа через форму регистрации
    def test_login_via_register_form(self, browser):
        browser.get(MAIN_PAGE_URL)
        browser.find_element(*REGISTER_BUTTON_MAIN_PAGE).click()
        wait = WebDriverWait(browser, 10)
        wait.until(EC.visibility_of_element_located(LOGIN_FORM_EMAIL_INPUT))
        browser.find_element(*LOGIN_FORM_EMAIL_INPUT).send_keys('existing_user@example.com')
        browser.find_element(*LOGIN_FORM_PASSWORD_INPUT).send_keys('valid_password')
        browser.find_element(*LOGIN_FORM_SUBMIT_BUTTON).click()
        wait.until(EC.visibility_of_element_located(PERSONAL_ACCOUNT_LINK))
        personal_account_text = browser.find_element(*PERSONAL_ACCOUNT_LINK).text
        assert personal_account_text == 'Личный кабинет'

    # Тест входа через форму восстановления пароля
    def test_login_via_reset_password_form(self, browser):
        browser.get(MAIN_PAGE_URL)
        browser.find_element(*FORGOT_PASSWORD_LINK).click()
        wait = WebDriverWait(browser, 10)
        wait.until(EC.visibility_of_element_located(LOGIN_FORM_EMAIL_INPUT))
        browser.find_element(*LOGIN_FORM_EMAIL_INPUT).send_keys('existing_user@example.com')
        browser.find_element(*LOGIN_FORM_PASSWORD_INPUT).send_keys('valid_password')
        browser.find_element(*LOGIN_FORM_SUBMIT_BUTTON).click()
        wait.until(EC.visibility_of_element_located(PERSONAL_ACCOUNT_LINK))
        personal_account_text = browser.find_element(*PERSONAL_ACCOUNT_LINK).text
        assert personal_account_text == 'Личный кабинет'
