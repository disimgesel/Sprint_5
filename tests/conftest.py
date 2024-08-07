from selenium import webdriver
import pytest
from data import Data
from data import Url
from locators import Locator
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture(scope='function')
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.get(Url.URL_HOME)
    yield chrome_driver
    chrome_driver.quit()


@pytest.fixture(scope='function')
def driver_login(driver):
    # На главной странице нажал на кнопку "Войти в аккаунт"
    driver.find_element(*Locator.LOGIN_TO_ACCOUT_BUTTON).click()
    # На странице входа ввел валидные данные и нажал кнопку "Войти"
    WebDriverWait(driver, Data.WAIT_TIME).until(EC.presence_of_element_located(Locator.CONDITION_LOGIN))
    driver.find_element(*Locator.ENTRY_FIELD_EMAIL_LOG).send_keys(Data.LOGIN_EMAIL)
    driver.find_element(*Locator.ENTRY_FIELD_PASSWORD_LOG).send_keys(Data.LOGIN_PASSWORD)
    driver.find_element(*Locator.BUTTON_LOGIN).click()
    yield driver

