from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators as lc


def test_link_to_constructor(driver, login):  # Проверка перехода по клику на «Конструктор» из ЛК

    # Клик по кнопке «Личный кабинет»
    driver.find_element(*lc.BUTTON_ACCOUNT).click()

    # Ожидание, что появился элемент с текстом "В этом разделе вы можете изменить свои персональные данные"
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(lc.ACCOUNT_TEXT))

    # Клик по кнопке «Конструктор»
    driver.find_element(*lc.BUTTON_CONST).click()

    # Ожидание, когда появится меню с булками на главной
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(lc.MENU_MAIN))

    # Проверка, что есть текст "Соберите бургер"
    assert driver.find_element(*lc.MAIN_TEXT).text == "Соберите бургер"


def test_link_to_logo(driver, login):  # Проверка перехода по клику на логотип Stellar Burgers

    # Клик по кнопке «Личный кабинет»
    driver.find_element(*lc.BUTTON_ACCOUNT).click()

    # Ожидание, что появился элемент с текстом "В этом разделе вы можете изменить свои персональные данные"
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(lc.ACCOUNT_TEXT))

    # Клик на логотип Stellar Burgers
    driver.find_element(*lc.LOGO).click()

    # Ожидание, когда появится меню с булками на главной
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(lc.MENU_MAIN))

    # Проверка, что есть текст "Соберите бургер"
    assert driver.find_element(*lc.MAIN_TEXT).text == "Соберите бургер"
