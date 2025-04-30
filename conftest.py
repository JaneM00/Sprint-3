# conftest.py

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope='function')
def browser():
    """Инициализирует веб-драйвер и закрывает его после окончания теста"""
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    browser = webdriver.Chrome(options=chrome_options)
    yield browser
    browser.quit()

@pytest.fixture(scope='session')
def browser():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    browser = webdriver.Chrome(options=chrome_options)
    yield browser
    browser.quit()
