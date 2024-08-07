from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locator
from data import Data
from conftest import driver


class TestKonstruktor:

    def test_to_bun_from_filling(self, driver):
        driver.find_element(*Locator.FILLING_IN_KONSTRUKTOR).click()
        WebDriverWait(driver, Data.WAIT_TIME).until(EC.presence_of_element_located(Locator.FILLING_IN_KONSTRUKTOR))
        driver.find_element(*Locator.BUN_IN_KONSTRUKTOR).click()
        WebDriverWait(driver, Data.WAIT_TIME).until(EC.presence_of_element_located(Locator.INGREDIENT_IN_BUN))
        display_bun = driver.find_element(*Locator.INGREDIENT_IN_BUN)
        active_bun = driver.find_element(*Locator.ACTIVE_BUN).get_attribute("class")
        assert display_bun.is_displayed()
        assert active_bun == Locator.ACTIVE_BUTTON

    def test_to_sauce_from_filling(self, driver):
        driver.find_element(*Locator.FILLING_IN_KONSTRUKTOR).click()
        WebDriverWait(driver, Data.WAIT_TIME).until(EC.presence_of_element_located(Locator.FILLING_IN_KONSTRUKTOR))
        driver.find_element(*Locator.SAUCE_IN_KONSTRUKTOR).click()
        WebDriverWait(driver, Data.WAIT_TIME).until(EC.presence_of_element_located(Locator.SAUCE_IN_KONSTRUKTOR))
        display_sauce = driver.find_element(*Locator.INGREDIENT_IN_SAUCE)
        active_sauce = driver.find_element(*Locator.ACTIVE_SAUCE).get_attribute("class")
        assert display_sauce.is_displayed()
        assert active_sauce == Locator.ACTIVE_BUTTON

    def test_to_filling_from_sauce(self, driver):
        driver.find_element(*Locator.SAUCE_IN_KONSTRUKTOR).click()
        WebDriverWait(driver, Data.WAIT_TIME).until(EC.presence_of_element_located(Locator.SAUCE_IN_KONSTRUKTOR))
        driver.find_element(*Locator.FILLING_IN_KONSTRUKTOR).click()
        WebDriverWait(driver, Data.WAIT_TIME).until(EC.presence_of_element_located(Locator.FILLING_IN_KONSTRUKTOR))
        display_filling = driver.find_element(*Locator.INGREDIENT_IN_FILLING)
        active_filling = driver.find_element(*Locator.ACTIVE_FILLING).get_attribute("class")
        assert display_filling.is_displayed()
        assert active_filling == Locator.ACTIVE_BUTTON
