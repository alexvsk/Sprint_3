from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import unittest
from locators import Locators as lc



class Link_to_constructor(unittest.TestCase):

    def setUp(self):

        self.driver = webdriver.Chrome()
        self.driver.get("https://stellarburgers.nomoreparties.site/login")

    def test_link_to_constructor(self):  # Проверка перехода по клику на «Конструктор» из ЛК

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

        # Клик по кнопке «Конструктор»
        self.driver.find_element(*lc.BUTTON_CONST).click()

        # Ожидание, когда появится меню с булками на главной
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(lc.MENU_MAIN))

        # Проверка, что есть текст "Соберите бургер"
        assert self.driver.find_element(*lc.MAIN_TEXT).text == "Соберите бургер"



    def test_link_to_logo(self):  # Проверка перехода по клику на логотип Stellar Burgers

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

        # Клик на логотип Stellar Burgers
        self.driver.find_element(*lc.LOGO).click()

        # Ожидание, когда появится меню с булками на главной
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(lc.MENU_MAIN))

        # Проверка, что есть текст "Соберите бургер"
        assert self.driver.find_element(*lc.MAIN_TEXT).text == "Соберите бургер"

    def tearDown(self):
            self.driver.quit()

if __name__ == "__main__":
    unittest.main()






