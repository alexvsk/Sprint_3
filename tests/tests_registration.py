from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators as lc
import unittest


class Registration(unittest.TestCase):

    def setUp(self):

        self.driver = webdriver.Chrome()
        self.driver.get("https://stellarburgers.nomoreparties.site/register")

    def test_reg_new_user(self):  # Проверка регистрации нового пользователя

        # Заполнение полей ввода
        self.driver.find_element(*lc.NAME_REG).send_keys("alex987")
        self.driver.find_element(*lc.EMAIL_REG).send_keys("alexpogonialin03987@ya.ru")
        self.driver.find_element(*lc.PASS_REG).send_keys("123456_!")
        self.driver.find_element(*lc.BUTTON_REG).click()

        # Ожидание, когда появится форма входа
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(lc.LOGIN_FORM))

    def test_wrong_pass_error(self):  # Проверка вывода ошибки для некорректного пароля

        # Заполнение полей ввода
        self.driver.find_element(*lc.NAME_REG).send_keys("mail")
        self.driver.find_element(*lc.EMAIL_REG).send_keys("Mail@mail.ru")
        self.driver.find_element(*lc.PASS_REG).send_keys("mail")
        self.driver.find_element(*lc.BUTTON_REG).click()

        # Ожидание, что поле ввода пароля подсветится красным цветом
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(lc.PASS_ERR))

        # Проверка текста ошибки
        assert self.driver.find_element(*lc.PASS_ERR_TEXT).text == "Некорректный пароль"

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
