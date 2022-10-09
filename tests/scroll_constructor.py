from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators as lc
import unittest

class Scroll_to_constructor(unittest.TestCase):

    def setUp(self):

        self.driver = webdriver.Chrome()
        self.driver.get("https://stellarburgers.nomoreparties.site/login")

    def test_track_to_sauces(self):  # Проверка перехода к разделу «Соусы»

        # Заполнение полей ввода
        self.driver.find_element(*lc.EMAIL_LOG).send_keys("alexpogonialin03555@ya.ru")
        self.driver.find_element(*lc.PASS_LOG).send_keys("123456_!")
        self.driver.find_element(*lc.BUTTON_LOG).click()

        # Ожидание, когда появится меню с булками на главной
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(lc.MENU_MAIN))

        # Прокрутка до последнего элемента в разделе соусы
        elem1 = self.driver.find_element(*lc.MENU_SOUSES)
        self.driver.execute_script("arguments[0].scrollIntoView();", elem1)

        # Проверка, что в атрибуте тега появился текст
        assert "tab_tab_type_current__2BEPc" in self.driver.find_element(*lc.ATTR_SOUSES).get_attribute('class')

    def test_track_to_rolls(self):  # Проверка перехода к разделу «Булки»

        # Заполнение полей ввода
        self.driver.find_element(*lc.EMAIL_LOG).send_keys("alexpogonialin03555@ya.ru")
        self.driver.find_element(*lc.PASS_LOG).send_keys("123456_!")
        self.driver.find_element(*lc.BUTTON_LOG).click()

        # Ожидание, когда появится меню с булками на главной
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(lc.MENU_MAIN))

        # Переход в соусы
        self.driver.find_element(*lc.SEC_SOUSES).click()

        # Прокрутка до последнего элемента в разделе булки
        elem1 = self.driver.find_element(*lc.MENU_ROLS)
        self.driver.execute_script("arguments[0].scrollIntoView();", elem1)

        # Проверка, что в атрибуте тега появился текст
        assert "tab_tab_type_current__2BEPc" in self.driver.find_element(*lc.ATTR_ROLLS).get_attribute('class')

    def test_track_to_top(self):  # Проверка перехода к разделу «Начинки»

    # Заполнение полей ввода
        self.driver.find_element(*lc.EMAIL_LOG).send_keys("alexpogonialin03555@ya.ru")
        self.driver.find_element(*lc.PASS_LOG).send_keys("123456_!")
        self.driver.find_element(*lc.BUTTON_LOG).click()

        # Ожидание, когда появится меню с булками на главной
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(lc.MENU_MAIN))

        # Прокрутка до последнего элемента в разделе начинки
        elem1 = self.driver.find_element(*lc.MENU_TOP)
        self.driver.execute_script("arguments[0].scrollIntoView();", elem1)

        # Проверка, что в атрибуте тега появился текст
        assert "tab_tab_type_current__2BEPc" in self.driver.find_element(*lc.ATTR_TOP).get_attribute('class')


    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
     unittest.main()
