# helpers.py

from locators import *

def perform_login(browser, email, password):
    """Выполняет процедуру входа пользователя"""
    browser.find_element(*LOGIN_FORM_EMAIL_INPUT).send_keys(email)
    browser.find_element(*LOGIN_FORM_PASSWORD_INPUT).send_keys(password)
    browser.find_element(*LOGIN_FORM_SUBMIT_BUTTON).click()

def perform_registration(browser, name, email, password):
    """Выполняет процедуру регистрации пользователя"""
    browser.find_element(*REGISTRATION_FORM_NAME_INPUT).send_keys(name)
    browser.find_element(*REGISTRATION_FORM_EMAIL_INPUT).send_keys(email)
    browser.find_element(*REGISTRATION_FORM_PASSWORD_INPUT).send_keys(password)
    browser.find_element(*REGISTRATION_FORM_SUBMIT_BUTTON).click()
