# tests/test_constructor.py
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import MAIN_PAGE_URL, BURGER_LOGO, CONSTRUCTOR_BUNS_SECTION, CONSTRUCTOR_SAUCE_SECTION, CONSTRUCTOR_FILLINGS_SECTION, ACTIVE_BUNS_TAB

class TestConstructor:

    # Тест открывания секции "Булки" в конструкторе
    def test_open_buns_section(self, browser):
        browser.get(MAIN_PAGE_URL)
        browser.find_element(*BURGER_LOGO).click()
        
        wait = WebDriverWait(browser, 10)
        wait.until(EC.visibility_of_element_located(CONSTRUCTOR_BUNS_SECTION))
        
        active_tab = browser.find_elements(*ACTIVE_BUNS_TAB).click()
        assert len(active_tab) > 0, "Активный таб 'Булки' не найден!"

    # Тест открывания секции "Соус"
    def test_open_sauce_section(self, browser):
        browser.get(MAIN_PAGE_URL)
        browser.find_element(*BURGER_LOGO).click()
        
        wait = WebDriverWait(browser, 10)
        wait.until(EC.element_to_be_clickable(CONSTRUCTOR_SAUCE_SECTION))
        browser.find_element(*CONSTRUCTOR_SAUCE_SECTION).click()
        
        active_tab = browser.find_elements(*ACTIVE_BUNS_TAB).click()
        assert len(active_tab) > 0, "Активный таб 'Соусы' не найден!"

    # Тест открывания секции "Начинка"
    def test_open_fillings_section(self, browser):
        browser.get(MAIN_PAGE_URL)
        browser.find_element(*BURGER_LOGO).click()
        
        wait = WebDriverWait(browser, 10)
        wait.until(EC.element_to_be_clickable(CONSTRUCTOR_FILLINGS_SECTION))
        browser.find_element(*CONSTRUCTOR_FILLINGS_SECTION).click()
        
        active_tab = browser.find_elements(*ACTIVE_BUNS_TAB).click()
        assert len(active_tab) > 0, "Активный таб 'Начинки' не найден!"
