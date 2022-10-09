from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import unittest
from locators import Locators as lc

class Link_to_account(unittest.TestCase):

    def setUp(self):

        self.driver = webdriver.Chrome()
        self.driver.get("https://stellarburgers.nomoreparties.site")

    def test_account_page(self):  # Проверка перехода по клику на «Личный кабинет».
        # Клик по кнопке «Войти в аккаунт»
        self.driver.find_element(*lc.BUTTON_LOG_MAIN).click()

        #Ожидание, когда появится форма входа
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(lc.LOGIN_FORM))

        # Заполнение полей ввода
        self.driver.find_element(*lc.EMAIL_LOG).send_keys("alexpogonialin03555@ya.ru")
        self.driver.find_element(*lc.PASS_LOG).send_keys("123456_!")
        self.driver.find_element(*lc.BUTTON_LOG).click()

        # Ожидание, когда появится меню с булками на главной
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(lc.MENU_MAIN))

        # Клик по кнопке «Личный кабинет»
        self.driver.find_element(*lc.BUTTON_ACCOUNT).click()

        # Ожидание, что появился элемент с текстом "В этом разделе вы можете изменить свои персональные данные"
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(lc.ACCOUNT_TEXT))

        # Проверка, что на странице ЛК есть кнопка "Выйти"
        assert self.driver.find_element(*lc.BUTTON_LOGOUT).text == "Выход"

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()