from selenium.webdriver.common.by import By

class Locator:
    LOGIN_TO_ACCOUT_BUTTON = (By.XPATH, ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']") # Кнопка "Войти в аккаунт"
    LINK_TO_REGISTRARION = (By.CLASS_NAME, "Auth_link__1fOlj")  # Гиперссылка "Зарегистрироваться"
    ENTRY_FIELD_NAME = (By.XPATH, ".//label[text() = 'Имя']/parent::*/input") # Поле ввода "Имя" при регистрации
    ENTRY_FIELD_EMAIL_REG = (By.XPATH, ".//label[text() = 'Email']/parent::*/input")  # Поле ввода "Email" при регистрации
    ENTRY_FIELD_PASSWORD = (By.XPATH, ".//label[text() = 'Пароль']/parent::*/input")  # Поле ввода "Пароль" при регистрации
    BUTTON_REGISTRATION = (By.XPATH, ".//button[text() ='Зарегистрироваться']")  # Кнопка "Зарегистрироваться"
    ENTRY_FIELD_EMAIL_LOG = (By.XPATH, ".//input[@name = 'name']") # Поле ввода "Email" при авторизации
    ENTRY_FIELD_PASSWORD_LOG = (By.XPATH, ".//input[@name = 'Пароль']") # Поле ввода "Пароль" при авторизации
    BUTTON_LOGIN = (By.XPATH, ".//button[text() ='Войти']")  # Кнопка "Войти"
    CONDITION_LOGIN = (By.XPATH, ".//h2[text() = 'Вход']") # Надпись "Вход" для явного ожидания на странице авторизации
    CONDITION_HOME = (By.XPATH, ".//h2[text() = 'Вход']") # Надпись "Вход" для явного ожидания на странице авторизации
    LINK_TO_PERSONAL_AREA = (By.XPATH, ".//p[text() = 'Личный Кабинет']") # Гиперссылка "Личный кабинет"
    LOGIN_IN_PERSONAL_AREA = (By.XPATH, ".//label[text() = 'Логин']/parent::*/input") # Поле "Логин" в личном кабинете
    MESSAGE_PASSWORD = (By.XPATH, ".//p[@class='input__error text_type_main-default']") # Сообщение о не валидном пароле
    LOGIN_IN_REGISTRATION = (By.XPATH, ".//a[text() = 'Войти']") # Гиперссылка "Войти" в форме регистрации
    RECOVERY_PASSWORD = (By.XPATH, ".//a[text() = 'Восстановить пароль']") # Гиперссылка "Восстановить пароль"
    LOGIN_RECOVERY_PASSWORD = (By.XPATH, ".//a[text() = 'Войти']") # Гиперссылка "Войти" на странице восстановления пароля
    LINK_KONSTRUKTOR = (By.XPATH, ".//p[text() = 'Конструктор']") # Раздел конструктор
    BUTTON_TO_EXIT = (By.XPATH, ".//button[text() = 'Выход']") # Кнопка "Выйти"
    FILLING_IN_KONSTRUKTOR =  (By.XPATH, ".//span[text()='Начинки']") # Начинки в контрукторе
    SAUCE_IN_KONSTRUKTOR = (By.XPATH, ".//span[text()='Соусы']")  # Соусы в контрукторе
    BUN_IN_KONSTRUKTOR = (By.XPATH, ".//span[text()='Булки']")  # Булки в контрукторе
    INGREDIENT_IN_BUN = (By.XPATH, ".//img[@alt='Краторная булка N-200i']") # Игнредиент в булках
    INGREDIENT_IN_SAUCE = (By.XPATH, ".//img[@alt='Соус традиционный галактический']")  # Игнредиент в соусах
    INGREDIENT_IN_FILLING = (By.XPATH, ".//img[@alt='Краторная булка N-200i']")  # Игнредиент в начинках
    ACTIVE_BUN = (By.XPATH, ".//span[text() = 'Булки']/parent::*")  # Активная кнопка "Булки"
    ACTIVE_SAUCE = (By.XPATH, ".//span[text() = 'Соусы']/parent::*")  # Активная кнопка "Соусы"
    ACTIVE_FILLING = (By.XPATH, ".//span[text() = 'Начинки']/parent::*")  # Активная кнопка "Начинки"
    LOGO_STELLAR_BURGERS = (By.XPATH, ".//div[@class='AppHeader_header__logo__2D0X2']/child::*") # Логитип Stellar Burgers
    ACTIVE_BUTTON = "tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect" # Проверка на активность вкладки конструктора
