from selenium import webdriver
import pytest
from data import Data
from locators import Locator
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture(scope='function')
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.get(Data.URL_HOME)
    yield chrome_driver
    chrome_driver.quit()


@pytest.fixture(scope='function')
def driver_login():
    chrome_driver = webdriver.Chrome()
    chrome_driver.get(Data.URL_HOME)
    # На главной странице нажал на кнопку "Войти в аккаунт"
    chrome_driver.find_element(*Locator.LOGIN_TO_ACCOUT_BUTTON).click()
    # На странице входа ввел валидные данные и нажал кнопку "Войти"
    WebDriverWait(chrome_driver, Data.WAIT_TIME).until(EC.presence_of_element_located(Locator.CONDITION_LOGIN))
    chrome_driver.find_element(*Locator.ENTRY_FIELD_EMAIL_LOG).send_keys(Data.LOGIN_EMAIL)
    chrome_driver.find_element(*Locator.ENTRY_FIELD_PASSWORD_LOG).send_keys(Data.LOGIN_PASSWORD)
    chrome_driver.find_element(*Locator.BUTTON_LOGIN).click()
    yield chrome_driver
    chrome_driver.quit()
