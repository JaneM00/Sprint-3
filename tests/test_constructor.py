# tests/test_constructor.py

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import MAIN_PAGE_URL, BURGER_LOGO, CONSTRUCTOR_BUNS_SECTION, ACTIVE_TAB_CLASS


@pytest.fixture(scope='session')
def browser():
    """Инициализирует веб-драйвер и возвращает объект"""
    from selenium import webdriver
    driver = webdriver.Chrome()  # Или другой драйвер по ситуации
    yield driver
    driver.quit()


class TestConstructor:

    # Тест открывания секции "Булки" в конструкторе
    def test_open_buns_section(self, browser):
        browser.get(MAIN_PAGE_URL)
        browser.find_element(*BURGER_LOGO).click()
        
        wait = WebDriverWait(browser, 10)
        wait.until(EC.visibility_of_element_located(CONSTRUCTOR_BUNS_SECTION))
        
        active_tab = browser.find_elements(By.CSS_SELECTOR, f'li[data-id="buns"].{ACTIVE_TAB_CLASS}')
        assert len(active_tab) > 0, "Активный таб 'Булки' не найден!"

    # Тест открывания секции "Соус"
    def test_open_sauce_section(self, browser):
        browser.get(MAIN_PAGE_URL)
        browser.find_element(*BURGER_LOGO).click()
        
        wait = WebDriverWait(browser, 10)
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'li[data-id="sauces"]')))
        browser.find_element(By.CSS_SELECTOR, 'li[data-id="sauces"]').click()
        
        active_tab = browser.find_elements(By.CSS_SELECTOR, f'li[data-id="sauces"].{ACTIVE_TAB_CLASS}')
        assert len(active_tab) > 0, "Активный таб 'Соусы' не найден!"

    # Тест открывания секции "Начинка"
    def test_open_fillings_section(self, browser):
        browser.get(MAIN_PAGE_URL)
        browser.find_element(*BURGER_LOGO).click()
        
        wait = WebDriverWait(browser, 10)
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'li[data-id="fillings"]')))
        browser.find_element(By.CSS_SELECTOR, 'li[data-id="fillings"]').click()
        
        active_tab = browser.find_elements(By.CSS_SELECTOR, f'li[data-id="fillings"].{ACTIVE_TAB_CLASS}')
        assert len(active_tab) > 0, "Активный таб 'Начинки' не найден!"
