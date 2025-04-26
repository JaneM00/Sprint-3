# tests/test_constructor.py

import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *

@pytest.mark.usefixtures("browser")
class TestConstructor:

    # Тест переключения вкладок в конструкторе
    def test_switch_tabs(self, browser):
        browser.get(MAIN_PAGE_URL)
        browser.find_element(*BURGER_LOGO).click()
        wait = WebDriverWait(browser, 10)
        wait.until(EC.visibility_of_element_located(NAVIGATION_ACTIVE_TAB))
        active_tab = browser.find_element(*NAVIGATION_ACTIVE_TAB)
        assert active_tab.text == 'Булки'

        # Переключение на соус
        browser.find_element(*CONSTRUCTOR_SAUCE_SECTION).click()
        wait.until(EC.visibility_of_element_located(NAVIGATION_ACTIVE_TAB))
        active_tab = browser.find_element(*NAVIGATION_ACTIVE_TAB)
        assert active_tab.text == 'Соусы'

        # Переключение на начинки
        browser.find_element(*CONSTRUCTOR_FILLINGS_SECTION).click()
        wait.until(EC.visibility_of_element_located(NAVIGATION_ACTIVE_TAB))
        active_tab = browser.find_element(*NAVIGATION_ACTIVE_TAB)
        assert active_tab.text == 'Начинки'
