from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locator
from data import Data
from conftest import driver


class TestLogin:

    def test_login_button_login_to_account(self, driver):
        # На главной странице нажал на кнопку "Войти в аккаунт"
        driver.find_element(*Locator.LOGIN_TO_ACCOUT_BUTTON).click()
        # На странице входа ввел валидные данные и нажал кнопку "Войти"
        WebDriverWait(driver, Data.WAIT_TIME).until(EC.presence_of_element_located(Locator.CONDITION_LOGIN))
        driver.find_element(*Locator.ENTRY_FIELD_EMAIL_LOG).send_keys(Data.LOGIN_EMAIL)
        driver.find_element(*Locator.ENTRY_FIELD_PASSWORD_LOG).send_keys(Data.LOGIN_PASSWORD)
        driver.find_element(*Locator.BUTTON_LOGIN).click()
        # Перешел в личный кабинет
        WebDriverWait(driver, Data.WAIT_TIME).until(EC.presence_of_element_located(Locator.LINK_TO_PERSONAL_AREA))
        driver.find_element(*Locator.LINK_TO_PERSONAL_AREA).click()
        # Проверка значения в поле "Логин"
        WebDriverWait(driver, Data.WAIT_TIME).until(EC.presence_of_element_located(Locator.LOGIN_IN_PERSONAL_AREA))
        fact_email = driver.find_element(*Locator.LOGIN_IN_PERSONAL_AREA).get_attribute('value')
        assert fact_email == Data.LOGIN_EMAIL

    def test_login_personal_area(self, driver):
        # На главной странице перешел в личный кабинет
        driver.find_element(*Locator.LINK_TO_PERSONAL_AREA).click()
        WebDriverWait(driver, Data.WAIT_TIME).until(EC.presence_of_element_located(Locator.CONDITION_LOGIN))
        # На странице входа ввел валидные данные и нажал кнопку "Войти"
        driver.find_element(*Locator.ENTRY_FIELD_EMAIL_LOG).send_keys(Data.LOGIN_EMAIL)
        driver.find_element(*Locator.ENTRY_FIELD_PASSWORD_LOG).send_keys(Data.LOGIN_PASSWORD)
        driver.find_element(*Locator.BUTTON_LOGIN).click()
        # Перешел в личный кабинет
        WebDriverWait(driver, Data.WAIT_TIME).until(EC.presence_of_element_located(Locator.LINK_TO_PERSONAL_AREA))
        driver.find_element(*Locator.LINK_TO_PERSONAL_AREA).click()
        # Проверка значения в поле "Логин"
        WebDriverWait(driver, Data.WAIT_TIME).until(EC.presence_of_element_located(Locator.LOGIN_IN_PERSONAL_AREA))
        fact_email = driver.find_element(*Locator.LOGIN_IN_PERSONAL_AREA).get_attribute('value')
        assert fact_email == Data.LOGIN_EMAIL

    def test_login_form_registration(self, driver):
        # На главной странице нажал на кнопку "Войти в аккаунт"
        driver.find_element(*Locator.LOGIN_TO_ACCOUT_BUTTON).click()
        WebDriverWait(driver, Data.WAIT_TIME).until(EC.presence_of_element_located(Locator.LINK_TO_REGISTRARION))
        # На странице входа перешел по гиперссылке "Зарегистрироваться"
        driver.find_element(*Locator.LINK_TO_REGISTRARION).click()
        WebDriverWait(driver, Data.WAIT_TIME).until(EC.presence_of_element_located(Locator.LOGIN_IN_REGISTRATION))
        # Нажал на гиперссылку "Войти"
        driver.find_element(*Locator.LOGIN_IN_REGISTRATION).click()
        # На странице входа ввел валидные данные и нажал кнопку "Войти"
        WebDriverWait(driver, Data.WAIT_TIME).until(EC.presence_of_element_located(Locator.CONDITION_LOGIN))
        driver.find_element(*Locator.ENTRY_FIELD_EMAIL_LOG).send_keys(Data.LOGIN_EMAIL)
        driver.find_element(*Locator.ENTRY_FIELD_PASSWORD_LOG).send_keys(Data.LOGIN_PASSWORD)
        driver.find_element(*Locator.BUTTON_LOGIN).click()
        # Перешел в личный кабинет
        WebDriverWait(driver, Data.WAIT_TIME).until(EC.presence_of_element_located(Locator.LINK_TO_PERSONAL_AREA))
        driver.find_element(*Locator.LINK_TO_PERSONAL_AREA).click()
        # Проверка значения в поле "Логин"
        WebDriverWait(driver, Data.WAIT_TIME).until(EC.presence_of_element_located(Locator.LOGIN_IN_PERSONAL_AREA))
        fact_email = driver.find_element(*Locator.LOGIN_IN_PERSONAL_AREA).get_attribute('value')
        assert fact_email == Data.LOGIN_EMAIL

    def test_login_recovery_password(self, driver):
        # На главной странице нажал на кнопку "Войти в аккаунт"
        driver.find_element(*Locator.LOGIN_TO_ACCOUT_BUTTON).click()
        WebDriverWait(driver, Data.WAIT_TIME).until(EC.presence_of_element_located(Locator.RECOVERY_PASSWORD))
        # На странице авторизации нажал на гиперссылку "Восстановить пароль"
        driver.find_element(*Locator.RECOVERY_PASSWORD).click()
        WebDriverWait(driver, Data.WAIT_TIME).until(EC.presence_of_element_located(Locator.LOGIN_RECOVERY_PASSWORD))
        # На странице восстановления пароля нажал на гиперссылку "Войти"
        driver.find_element(*Locator.LOGIN_RECOVERY_PASSWORD).click()
        # На странице входа ввел валидные данные и нажал кнопку "Войти"
        WebDriverWait(driver, Data.WAIT_TIME).until(EC.presence_of_element_located(Locator.CONDITION_LOGIN))
        driver.find_element(*Locator.ENTRY_FIELD_EMAIL_LOG).send_keys(Data.LOGIN_EMAIL)
        driver.find_element(*Locator.ENTRY_FIELD_PASSWORD_LOG).send_keys(Data.LOGIN_PASSWORD)
        driver.find_element(*Locator.BUTTON_LOGIN).click()
        # Перешел в личный кабинет
        WebDriverWait(driver, Data.WAIT_TIME).until(EC.presence_of_element_located(Locator.LINK_TO_PERSONAL_AREA))
        driver.find_element(*Locator.LINK_TO_PERSONAL_AREA).click()
        # Проверка значения в поле "Логин"
        WebDriverWait(driver, Data.WAIT_TIME).until(EC.presence_of_element_located(Locator.LOGIN_IN_PERSONAL_AREA))
        fact_email = driver.find_element(*Locator.LOGIN_IN_PERSONAL_AREA).get_attribute('value')
        assert fact_email == Data.LOGIN_EMAIL
