from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators as lc
import unittest

class Login(unittest.TestCase):

    def setUp(self):

        self.driver = webdriver.Chrome()
        self.driver.get("https://stellarburgers.nomoreparties.site")


    def test_login_main_page(self):  # Проверка входа по кнопке «Войти в аккаунт» на главной
        # Запоминаем текст кнопки на главной странице до авторизации ("Войти в аккаунт")
        button_text_before = self.driver.find_element(*lc.BUTTON_LOG_MAIN).text
        # Клик по кнопке «Войти в аккаунт»
        self.driver.find_element(*lc.BUTTON_LOG_MAIN).click()
        # Ожидание, когда появится форма входа
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(lc.LOGIN_FORM))
        # Заполнение полей ввода
        self.driver.find_element(*lc.EMAIL_LOG).send_keys("alexpogonialin03555@ya.ru")
        self.driver.find_element(*lc.PASS_LOG).send_keys("123456_!")
        self.driver.find_element(*lc.BUTTON_LOG).click()
        # Ожидание, когда появится меню с булками на главной
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(lc.MENU_MAIN))
        # Запоминаем текст кнопки на главной странице после авторизации ("Оформить заказ")
        button_text_after = self.driver.find_element(*lc.BUTTON_LOG_MAIN).text
        # Проверка, что после авторизации текст кнопки изменился
        assert button_text_after != button_text_before


    def test_login_account_page(self):  # Проверка входа через кнопку «Личный кабинет»
        # Запоминаем текст кнопки на главной странице до авторизации ("Войти в аккаунт")
        button_text_before = self.driver.find_element(*lc.BUTTON_LOG_MAIN).text
        # Клик по кнопке «Личный кабинет»
        self.driver.find_element(*lc.BUTTON_ACCOUNT).click()
        # Ожидание, когда появится форма входа
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(lc.LOGIN_FORM))
        # Заполнение полей ввода
        self.driver.find_element(*lc.EMAIL_LOG).send_keys("alexpogonialin03555@ya.ru")
        self.driver.find_element(*lc.PASS_LOG).send_keys("123456_!")
        self.driver.find_element(*lc.BUTTON_LOG).click()
        # Ожидание, когда появится меню с булками на главной
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(lc.MENU_MAIN))
        # Запоминаем текст кнопки на главной странице после авторизации ("Оформить заказ")
        button_text_after = self.driver.find_element(*lc.BUTTON_LOG_MAIN).text
        # Проверка, что после авторизации текст кнопки изменился
        assert button_text_after != button_text_before


    def test_login_register_page(self):  # Проверка входа через кнопку в форме регистрации
        # Запоминаем текст кнопки на главной странице до авторизации ("Войти в аккаунт")
        button_text_before = self.driver.find_element(*lc.BUTTON_LOG_MAIN).text
        # Клик по кнопке «Личный кабинет»
        self.driver.find_element(*lc.BUTTON_ACCOUNT).click()
        # Клик по кнопке «Зарегистрироваться»
        self.driver.find_element(*lc.BUTTON_REG1).click()
        # Клик по кнопке «Войти»
        self.driver.find_element(*lc.BUTTON_LOG1).click()
        # Ожидание, когда появится форма входа
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(lc.LOGIN_FORM))
        # Заполнение полей ввода
        self.driver.find_element(*lc.EMAIL_LOG).send_keys("alexpogonialin03555@ya.ru")
        self.driver.find_element(*lc.PASS_LOG).send_keys("123456_!")
        self.driver.find_element(*lc.BUTTON_LOG).click()
        # Ожидание, когда появится меню с булками на главной
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(lc.MENU_MAIN))
        # Запоминаем текст кнопки на главной странице после авторизации ("Оформить заказ")
        button_text_after = self.driver.find_element(*lc.BUTTON_LOG_MAIN).text
        # Проверка, что после авторизации текст кнопки изменился
        assert button_text_after != button_text_before

    def test_login_password_forgot_page(self):  # Проверка входа через кнопку в форме восстановления пароля
        # Запоминаем текст кнопки на главной странице до авторизации ("Войти в аккаунт")
        button_text_before = self.driver.find_element(*lc.BUTTON_LOG_MAIN).text
        # Клик по кнопке «Личный кабинет»
        self.driver.find_element(By.XPATH, ".//a[@href='/account'][last()]").click()
        # Клик по кнопке «Восстановить пароль»
        self.driver.find_element(*lc.BUTTON_PASS_FORGOT).click()
        # Клик по кнопке «Войти»
        self.driver.find_element(*lc.BUTTON_LOG1).click()
        # Ожидание, когда появится форма входа
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(lc.LOGIN_FORM))
        # Заполнение полей ввода
        self.driver.find_element(*lc.EMAIL_LOG).send_keys("alexpogonialin03555@ya.ru")
        self.driver.find_element(*lc.PASS_LOG).send_keys("123456_!")
        self.driver.find_element(*lc.BUTTON_LOG).click()
        # Ожидание, когда появится меню с булками на главной
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(lc.MENU_MAIN))
        # Запоминаем текст кнопки на главной странице после авторизации ("Оформить заказ")
        button_text_after = self.driver.find_element(*lc.BUTTON_LOG_MAIN).text
        # Проверка, что после авторизации текст кнопки изменился
        assert button_text_after != button_text_before

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()