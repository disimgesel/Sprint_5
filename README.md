# qa_python_5
Проект содержит UI тесты для web-приложения "Stellar Burgers", URL = https://stellarburgers.nomoreparties.site/
В директории tests находятся файлы с тестами:
    - test_konstruktor:
        - def test_to_bun_from_filling (Переход из раздела Начинки в раздел Булки)
        - def test_to_sauce_from_filling (Переход из раздела Начинки в раздел Соусы)
        - def test_to_filling_from_sauce (Переход из раздела Соусы в раздел Начинки)
    - test_login:
        - def test_login_button_login_to_account (Авторизация по кнопке «Войти в аккаунт» на главной)
        - def test_login_personal_area (Авторизация через кнопку «Личный кабинет»)
        - def test_login_form_registration (Авторизания ерез кнопку в форме регистрации)
        - def test_login_recovery_password (Авторизания через кнопку в форме восстановления пароля)
    - test_registration:
        - def test_registration_valid_pswd (Успешная регистрация с валидными данными)
        - def test_registration_invalid_pswd (Получение ошибки с не валидным паролем при регистрации)
    - test_navigation:
        - def test_navigation_in_personal_area (Переход по клику в «Личный кабинет»)
        - def test_navigation_from_personal_area_to_konstruktor (Переход по клику в «Конструктор»)
        - def test_navigation_from_personal_area_to_stellar_burgers (Переход по клику на Stellar Burgers в «Конструктор»)
        - def test_exit_from_personal_area (Выход по кнопке «Выйти» в личном кабинете)
В корневой директории Sprint_5 находятся файлы:
    - .gitignore
    - conftests
    - data
    - helpers
    - locators
    - README