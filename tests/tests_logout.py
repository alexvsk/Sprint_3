
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators as lc

def test_logout_from_account_page(driver, login):  # Проверка выхода по кнопке «Выйти» в личном кабинете.

    # Клик по кнопке «Личный кабинет»
    driver.find_element(*lc.BUTTON_ACCOUNT).click()

    # Ожидание, что появился элемент с текстом "В этом разделе вы можете изменить свои персональные данные"
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(lc.ACCOUNT_TEXT))

    # Клик по кнопке "Выйти"
    driver.find_element(*lc.BUTTON_LOGOUT).click()

    driver.implicitly_wait(3)

    # Проверка, что появилась форма авторизации
    assert "Auth_login" in driver.find_element(*lc.LOGIN_FORM).get_attribute("class")

