# helpers.py

from locators import *

def perform_login(browser, email, password):
    browser.find_element(*LOGIN_FORM_EMAIL_INPUT).send_keys(email)
    browser.find_element(*LOGIN_FORM_PASSWORD_INPUT).send_keys(password)
    browser.find_element(*LOGIN_FORM_SUBMIT_BUTTON).click()
