# locators.py

from selenium.webdriver.common.by import By

# Базовый URL сайта
MAIN_PAGE_URL = 'https://stellarburgers.nomoreparties.site/'

# Главный экран
BURGER_LOGO = (By.CLASS_NAME, 'AppHeader_header__logo__2TDzT')
LOGIN_BUTTON_MAIN_PAGE = (By.CSS_SELECTOR, 'a[href="/login"]')
REGISTER_BUTTON_MAIN_PAGE = (By.CSS_SELECTOR, 'a[href="/register"]')
PERSONAL_ACCOUNT_LINK = (By.CSS_SELECTOR, '.AppHeader_header__linkText__bZTlX.AppHeader_header__link__1f_O6')

# Форма входа
LOGIN_FORM_EMAIL_INPUT = (By.NAME, 'email')
LOGIN_FORM_PASSWORD_INPUT = (By.NAME, 'password')
LOGIN_FORM_SUBMIT_BUTTON = (By.CSS_SELECTOR, 'button[type="submit"]')

# Форма регистрации
REGISTRATION_FORM_NAME_INPUT = (By.NAME, 'name')
REGISTRATION_FORM_EMAIL_INPUT = (By.NAME, 'email')
REGISTRATION_FORM_PASSWORD_INPUT = (By.NAME, 'password')
REGISTRATION_FORM_SUBMIT_BUTTON = (By.CSS_SELECTOR, 'button[type="submit"]')

# Личный кабинет
PERSONAL_ACCOUNT_LOGOUT_BUTTON = (By.CSS_SELECTOR, '.profile-form__exit')

# Сообщения об ошибках
ERROR_MESSAGE_ELEMENT = (By.CLASS_NAME, 'input__error')

# Конструктор бургера
CONSTRUCTOR_BUNS_SECTION = (By.ID, 'buns')
CONSTRUCTOR_SAUCE_SECTION = (By.ID, 'sauces')
CONSTRUCTOR_FILLINGS_SECTION = (By.ID, 'fillings')

# Классы активных состояний 
ACTIVE_TAB_CLASS = 'current'

# Локатор для ссылки восстановления пароля
FORGOT_PASSWORD_LINK = (By.LINK_TEXT, "Восстановить пароль")
