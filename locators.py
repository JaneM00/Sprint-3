from selenium.webdriver.common.by import By

# Главные локаторы
MAIN_PAGE_URL = 'https://stellarburgers.nomoreparties.site/'
BURGER_LOGO = (By.CSS_SELECTOR, '.AppHeader_header__logo__2TDzT')
LOGIN_BUTTON_MAIN_PAGE = (By.CSS_SELECTOR, '[href="/login"]')
REGISTER_BUTTON_MAIN_PAGE = (By.CSS_SELECTOR, '[href="/register"]')
PERSONAL_ACCOUNT_LINK = (By.CSS_SELECTOR, '.AppHeader_header__linkText__bZTlX.AppHeader_header__link__1f_O6')

# Формы ввода и кнопки
LOGIN_FORM_EMAIL_INPUT = (By.NAME, 'email')
LOGIN_FORM_PASSWORD_INPUT = (By.NAME, 'password')
LOGIN_FORM_SUBMIT_BUTTON = (By.CSS_SELECTOR, 'button[type="submit"]')

# Конструктор
CONSTRUCTOR_BUNS_SECTION = (By.ID, 'buns')
CONSTRUCTOR_SAUCE_SECTION = (By.ID, 'sauces')
CONSTRUCTOR_FILLINGS_SECTION = (By.ID, 'fillings')

# Личный кабинет
PERSONAL_ACCOUNT_LOGOUT_BUTTON = (By.CSS_SELECTOR, '.profile-form__exit')
FORGOT_PASSWORD_LINK = (By.LINK_TEXT, 'Забыли пароль?')

# Элементы активного состояния (для проверок)
ACTIVE_TAB_CLASS = 'current'
