from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locator
from data import Data
from conftest import driver


class TestRegistration:

    def test_registration_valid_pswd(self, driver):
        # На главной странице нажал на кнопку "Войти в аккаунт"
        driver.find_element(*Locator.LOGIN_TO_ACCOUT_BUTTON).click()
        WebDriverWait(driver, Data.WAIT_TIME).until(EC.presence_of_element_located(Locator.LINK_TO_REGISTRARION))
        # На странице входа перешел по гиперссылке "Зарегистрироваться"
        driver.find_element(*Locator.LINK_TO_REGISTRARION).click()
        # Ввел данные для регистрации
        WebDriverWait(driver, Data.WAIT_TIME).until(EC.presence_of_element_located(Locator.ENTRY_FIELD_NAME))
        driver.find_element(*Locator.ENTRY_FIELD_NAME).send_keys(Data.REGISTRATION_NAME)
        registration_email = Data.REGISTRATION_EMAIL
        driver.find_element(*Locator.ENTRY_FIELD_EMAIL_REG).send_keys(registration_email)
        driver.find_element(*Locator.ENTRY_FIELD_PASSWORD).send_keys(Data.REGISTRATION_PASSWORD_VALID)
        # Нажал кнопку "Зарегистрироваться"
        driver.find_element(*Locator.BUTTON_REGISTRATION).click()
        # На странице входа ввел валидные данные и нажал кнопку "Войти" с изспользованием явного ожидания
        WebDriverWait(driver, Data.WAIT_TIME).until(EC.presence_of_element_located(Locator.CONDITION_LOGIN))
        driver.find_element(*Locator.ENTRY_FIELD_EMAIL_LOG).send_keys(registration_email)
        driver.find_element(*Locator.ENTRY_FIELD_PASSWORD_LOG).send_keys(Data.REGISTRATION_PASSWORD_VALID)
        driver.find_element(*Locator.BUTTON_LOGIN).click()
        # Перешел в личный кабинет
        WebDriverWait(driver, Data.WAIT_TIME).until(EC.presence_of_element_located(Locator.LINK_TO_PERSONAL_AREA))
        driver.find_element(*Locator.LINK_TO_PERSONAL_AREA).click()
        # Проверка значения в поле "Логин"
        WebDriverWait(driver, Data.WAIT_TIME).until(EC.presence_of_element_located(Locator.LOGIN_IN_PERSONAL_AREA))
        fact_email = driver.find_element(*Locator.LOGIN_IN_PERSONAL_AREA).get_attribute('value')
        assert fact_email == registration_email

    def test_registration_invalid_pswd(self, driver):
        # На главной странице нажал на кнопку "Войти в аккаунт"
        driver.find_element(*Locator.LOGIN_TO_ACCOUT_BUTTON).click()
        WebDriverWait(driver, Data.WAIT_TIME).until(EC.presence_of_element_located(Locator.LINK_TO_REGISTRARION))
        # На странице входа перешел по гиперссылке "Зарегистрироваться"
        driver.find_element(*Locator.LINK_TO_REGISTRARION).click()
        # Ввел данные для регистрации с не валидным паролем
        WebDriverWait(driver, Data.WAIT_TIME).until(EC.presence_of_element_located(Locator.ENTRY_FIELD_NAME))
        driver.find_element(*Locator.ENTRY_FIELD_NAME).send_keys(Data.REGISTRATION_NAME)
        registration_email = Data.REGISTRATION_EMAIL
        driver.find_element(*Locator.ENTRY_FIELD_EMAIL_REG).send_keys(registration_email)
        driver.find_element(*Locator.ENTRY_FIELD_PASSWORD).send_keys(Data.REGISTRATION_PASSWORD_INVALID)
        # Нажал кнопку "Зарегистрироваться"
        driver.find_element(*Locator.BUTTON_REGISTRATION).click()
        text_about_pswd = driver.find_element(*Locator.MESSAGE_PASSWORD).text
        assert text_about_pswd == Data.TEXT_INVALID_PASSWORD
