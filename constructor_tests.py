import time
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *

class ConstructorTests(unittest.TestCase):

    def setUp(self):
        pass  # Всё управление браузером передано в фикстуру

    def tearDown(self):
        pass  # Всё управление браузером передано в фикстуру

    # Тест открытия раздела "Булки" в конструкторе
    def test_open_buns_section(self, browser):
        browser.get(MAIN_PAGE_URL)
        browser.find_element(*BURGER_LOGO).click()
        wait = WebDriverWait(browser, 10)
        wait.until(EC.visibility_of_element_located(CONSTRUCTOR_BUNS_SECTION))
        active_tab = browser.find_elements_by_css_selector(f'li[data-id="buns"].{ACTIVE_TAB_CLASS}')
        self.assertGreater(len(active_tab), 0, "Активный таб 'Булки' не найден!")

    # Аналогично делаем для остальных разделов
    def test_open_sauce_section(self, browser):
        browser.get(MAIN_PAGE_URL)
        browser.find_element(*BURGER_LOGO).click()
        wait = WebDriverWait(browser, 10)
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'li[data-id="sauces"]')))
        browser.find_element_by_css_selector('li[data-id="sauces"]').click()
        active_tab = browser.find_elements_by_css_selector(f'li[data-id="sauces"].{ACTIVE_TAB_CLASS}')
        self.assertGreater(len(active_tab), 0, "Активный таб 'Соусы' не найден!")

    def test_open_fillings_section(self, browser):
        browser.get(MAIN_PAGE_URL)
        browser.find_element(*BURGER_LOGO).click()
        wait = WebDriverWait(browser, 10)
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'li[data-id="fillings"]')))
        browser.find_element_by_css_selector('li[data-id="fillings"]').click()
        active_tab = browser.find_elements_by_css_selector(f'li[data-id="fillings"].{ACTIVE_TAB_CLASS}')
        self.assertGreater(len(active_tab), 0, "Активный таб 'Начинки' не найден!")
