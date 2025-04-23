import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope='session')
def browser():
    """Инициализирует веб-драйвер и закрывает его после завершения сессии."""
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    browser = webdriver.Chrome(options=chrome_options)
    yield browser
    browser.quit()
