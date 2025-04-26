# tests/test_personal_account.py

import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *
from helpers import perform_login

@pytest.mark.usefixtures("browser")
class TestPersonalAccount:

    # Тест перехода в личный кабинет по ссылке "Личный кабинет"
    def test_personal_account_link_click(self, browser):
        browser.get(MAIN_PAGE_URL)
        browser.find_element(*PERSONAL_ACCOUNT_LINK).click()
        wait = WebDriverWait(browser, 10)
        wait.until(EC.visibility_of_element_located(LOGIN_FORM_EMAIL_INPUT))  # Появилась форма авторизации
        perform_login(browser, 'existing_user@example.com', 'valid_password')
        wait.until(EC.visibility_of_element_located(PERSONAL_ACCOUNT_LINK))
        personal_account_text = browser.find_element(*PERSONAL_ACCOUNT_LINK).text
        assert personal_account_text == 'Личный кабинет'

    # Тест выхода из аккаунта
    def test_logout(self, browser):
        browser.get(MAIN_PAGE_URL)
        browser.find_element(*PERSONAL_ACCOUNT_LINK).click()
        wait = WebDriverWait(browser, 10)
        wait.until(EC.visibility_of_element_located(LOGIN_FORM_EMAIL_INPUT))  # Появилась форма авторизации
        perform_login(browser, 'existing_user@example.com', 'valid_password')
        wait.until(EC.visibility_of_element_located(PERSONAL_ACCOUNT_LINK))
        browser.find_element(*PERSONAL_ACCOUNT_LOGOUT_BUTTON).click()
        wait.until(EC.invisibility_of_element_located(PERSONAL_ACCOUNT_LINK))  # Личный кабинет исчез
        logout_success_text = browser.find_element(*LOGIN_BUTTON_MAIN_PAGE).text
        assert logout_success_text == 'Войти в аккаунт'
