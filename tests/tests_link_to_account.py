from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators as lc

def test_account_page(driver, login):  # Проверка перехода по клику на «Личный кабинет».

    # Клик по кнопке «Личный кабинет»
    driver.find_element(*lc.BUTTON_ACCOUNT).click()

    # Ожидание, что появился элемент с текстом "В этом разделе вы можете изменить свои персональные данные"
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(lc.ACCOUNT_TEXT))

    # Проверка, что на странице ЛК есть кнопка "Выйти"
    assert driver.find_element(*lc.BUTTON_LOGOUT).text == "Выход"
