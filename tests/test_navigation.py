from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locator
from data import Data
from data import Url
from conftest import driver_login


class TestNavigatoin:

    def test_navigation_in_personal_area(self, driver_login):
        # На главной странице перешел в личный кабинет
        driver_login.find_element(*Locator.LINK_TO_PERSONAL_AREA).click()
        WebDriverWait(driver_login, Data.WAIT_TIME).until(EC.presence_of_element_located(Locator.LINK_TO_PERSONAL_AREA))
        current_url = driver_login.current_url
        assert current_url == Url.URL_PERSONAL_AREA

    def test_navigation_from_personal_area_to_konstruktor(self, driver_login):
        # На главной странице перешел в личный кабинет
        driver_login.find_element(*Locator.LINK_TO_PERSONAL_AREA).click()
        WebDriverWait(driver_login, Data.WAIT_TIME).until(EC.presence_of_element_located(Locator.LINK_TO_PERSONAL_AREA))
        # Перешел в радел "Конструктор"
        driver_login.find_element(*Locator.LINK_KONSTRUKTOR).click()
        WebDriverWait(driver_login, Data.WAIT_TIME).until(EC.presence_of_element_located(Locator.LINK_TO_PERSONAL_AREA))
        current_url_konsrt = driver_login.current_url
        assert current_url_konsrt == Url.URL_KONSTRUKTOR

    def test_navigation_from_personal_area_to_stellar_burgers(self, driver_login):
        # На главной странице перешел в личный кабинет
        driver_login.find_element(*Locator.LINK_TO_PERSONAL_AREA).click()
        WebDriverWait(driver_login, Data.WAIT_TIME).until(EC.presence_of_element_located(Locator.LINK_TO_PERSONAL_AREA))
        # Перешел в раздел "Конструктор" по клику на "Stellar Burgers"
        driver_login.find_element(*Locator.LOGO_STELLAR_BURGERS).click()
        WebDriverWait(driver_login, Data.WAIT_TIME).until(EC.presence_of_element_located(Locator.LINK_TO_PERSONAL_AREA))
        current_url_stellar = driver_login.current_url
        assert current_url_stellar == Url.URL_KONSTRUKTOR

    def test_exit_from_personal_area(self, driver_login):
        # На главной странице перешел в личный кабинет
        driver_login.find_element(*Locator.LINK_TO_PERSONAL_AREA).click()
        # В личном кабинете нажал кнопку "Выйти"
        WebDriverWait(driver_login, Data.WAIT_TIME).until(EC.presence_of_element_located(Locator.BUTTON_TO_EXIT))
        driver_login.find_element(*Locator.BUTTON_TO_EXIT).click()
        WebDriverWait(driver_login, Data.WAIT_TIME).until(EC.presence_of_element_located(Locator.CONDITION_LOGIN))
        current_url_exit = driver_login.current_url
        assert current_url_exit == Url.URL_EXIT
