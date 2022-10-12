from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators as lc

def test_login_main_page(driver):  # Проверка входа по кнопке «Войти в аккаунт» на главной\

    driver.get("https://stellarburgers.nomoreparties.site")

    # Запоминаем текст кнопки на главной странице до авторизации ("Войти в аккаунт")
    button_text_before = driver.find_element(*lc.BUTTON_LOG_MAIN).text

    # Клик по кнопке «Войти в аккаунт»
    driver.find_element(*lc.BUTTON_LOG_MAIN).click()

    # Ожидание, когда появится форма входа
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(lc.LOGIN_FORM))

    # Заполнение полей ввода
    driver.find_element(*lc.EMAIL_LOG).send_keys("alexpogonialin03555@ya.ru")
    driver.find_element(*lc.PASS_LOG).send_keys("123456_!")
    driver.find_element(*lc.BUTTON_LOG).click()

    # Ожидание, когда появится меню с булками на главной
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(lc.MENU_MAIN))

    # Запоминаем текст кнопки на главной странице после авторизации ("Оформить заказ")
    button_text_after = driver.find_element(*lc.BUTTON_LOG_MAIN).text

    # Проверка, что после авторизации текст кнопки изменился
    assert button_text_after != button_text_before


def test_login_account_page(driver):  # Проверка входа через кнопку «Личный кабинет»

    driver.get("https://stellarburgers.nomoreparties.site")

    # Запоминаем текст кнопки на главной странице до авторизации ("Войти в аккаунт")
    button_text_before = driver.find_element(*lc.BUTTON_LOG_MAIN).text

    # Клик по кнопке «Личный кабинет»
    driver.find_element(*lc.BUTTON_ACCOUNT).click()

    # Ожидание, когда появится форма входа
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(lc.LOGIN_FORM))

    # Заполнение полей ввода
    driver.find_element(*lc.EMAIL_LOG).send_keys("alexpogonialin03555@ya.ru")
    driver.find_element(*lc.PASS_LOG).send_keys("123456_!")
    driver.find_element(*lc.BUTTON_LOG).click()

    # Ожидание, когда появится меню с булками на главной
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(lc.MENU_MAIN))

    # Запоминаем текст кнопки на главной странице после авторизации ("Оформить заказ")
    button_text_after = driver.find_element(*lc.BUTTON_LOG_MAIN).text

    # Проверка, что после авторизации текст кнопки изменился
    assert button_text_after != button_text_before


def test_login_register_page(driver):  # Проверка входа через кнопку в форме регистрации

    driver.get("https://stellarburgers.nomoreparties.site")

    # Запоминаем текст кнопки на главной странице до авторизации ("Войти в аккаунт")
    button_text_before = driver.find_element(*lc.BUTTON_LOG_MAIN).text

    # Клик по кнопке «Личный кабинет»
    driver.find_element(*lc.BUTTON_ACCOUNT).click()

    # Клик по кнопке «Зарегистрироваться»
    driver.find_element(*lc.BUTTON_REG1).click()

    # Клик по кнопке «Войти»
    driver.find_element(*lc.BUTTON_LOG1).click()

    # Ожидание, когда появится форма входа
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(lc.LOGIN_FORM))

    # Заполнение полей ввода
    driver.find_element(*lc.EMAIL_LOG).send_keys("alexpogonialin03555@ya.ru")
    driver.find_element(*lc.PASS_LOG).send_keys("123456_!")
    driver.find_element(*lc.BUTTON_LOG).click()

    # Ожидание, когда появится меню с булками на главной
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(lc.MENU_MAIN))

    # Запоминаем текст кнопки на главной странице после авторизации ("Оформить заказ")
    button_text_after = driver.find_element(*lc.BUTTON_LOG_MAIN).text

    # Проверка, что после авторизации текст кнопки изменился
    assert button_text_after != button_text_before

def test_login_password_forgot_page(driver):  # Проверка входа через кнопку в форме восстановления пароля

    driver.get("https://stellarburgers.nomoreparties.site")

    # Запоминаем текст кнопки на главной странице до авторизации ("Войти в аккаунт")
    button_text_before = driver.find_element(*lc.BUTTON_LOG_MAIN).text

    # Клик по кнопке «Личный кабинет»
    driver.find_element(*lc.BUTTON_ACCOUNT).click()

    # Клик по кнопке «Восстановить пароль»
    driver.find_element(*lc.BUTTON_PASS_FORGOT).click()

    # Клик по кнопке «Войти»
    driver.find_element(*lc.BUTTON_LOG1).click()

    # Ожидание, когда появится форма входа
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(lc.LOGIN_FORM))

    # Заполнение полей ввода
    driver.find_element(*lc.EMAIL_LOG).send_keys("alexpogonialin03555@ya.ru")
    driver.find_element(*lc.PASS_LOG).send_keys("123456_!")
    driver.find_element(*lc.BUTTON_LOG).click()

    # Ожидание, когда появится меню с булками на главной
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(lc.MENU_MAIN))

    # Запоминаем текст кнопки на главной странице после авторизации ("Оформить заказ")
    button_text_after = driver.find_element(*lc.BUTTON_LOG_MAIN).text

    # Проверка, что после авторизации текст кнопки изменился
    assert button_text_after != button_text_before
