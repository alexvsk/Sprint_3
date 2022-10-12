from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators as lc
def test_reg_new_user(driver):  # Проверка регистрации нового пользователя
    driver.get("https://stellarburgers.nomoreparties.site/register")

    # Заполнение полей ввода
    driver.find_element(*lc.NAME_REG).send_keys("alex987")
    driver.find_element(*lc.EMAIL_REG).send_keys("alexpogonialin03985@ya.ru")
    driver.find_element(*lc.PASS_REG).send_keys("123456_!")
    driver.find_element(*lc.BUTTON_REG).click()

    driver.implicitly_wait(3)

    # Проверка, что появилась форма авторизации
    assert "Auth_login" in driver.find_element(*lc.LOGIN_FORM).get_attribute("class")

def test_wrong_pass_error(driver):  # Проверка вывода ошибки для некорректного пароля
    driver.get("https://stellarburgers.nomoreparties.site/register")

    # Заполнение полей ввода
    driver.find_element(*lc.NAME_REG).send_keys("mail")
    driver.find_element(*lc.EMAIL_REG).send_keys("Mail@mail.ru")
    driver.find_element(*lc.PASS_REG).send_keys("mail")

    driver.find_element(*lc.BUTTON_REG).click()

    # Ожидание, что поле ввода пароля подсветится красным цветом
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(lc.PASS_ERR))

    # Проверка текста ошибки
    assert driver.find_element(*lc.PASS_ERR_TEXT).text == "Некорректный пароль"
