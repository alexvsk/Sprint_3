import pytest
from selenium import webdriver
from locators import Locators as lc
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

@pytest.fixture()
def driver():
    _driver = webdriver.Chrome()
    yield _driver
    _driver.quit()

@pytest.fixture()
def login(driver):
    driver.get("https://stellarburgers.nomoreparties.site/login")
    # Заполнение полей ввода
    driver.find_element(*lc.EMAIL_LOG).send_keys("alexpogonialin03555@ya.ru")
    driver.find_element(*lc.PASS_LOG).send_keys("123456_!")
    driver.find_element(*lc.BUTTON_LOG).click()
    # Ожидание, когда появится меню с булками на главной
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(lc.MENU_MAIN))
