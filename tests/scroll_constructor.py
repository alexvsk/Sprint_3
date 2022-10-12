from locators import Locators as lc

def test_track_to_sauces(driver, login):  # Проверка перехода к разделу «Соусы»

    # Прокрутка до последнего элемента в разделе соусы
    elem1 = driver.find_element(*lc.MENU_SOUSES)
    driver.execute_script("arguments[0].scrollIntoView();", elem1)

    # Проверка, что в атрибуте тега появился текст (кнопка "соусы" выбрана)
    assert "tab_tab_type_current__2BEPc" in driver.find_element(*lc.ATTR_SOUSES).get_attribute('class')

def test_track_to_rolls(driver, login):  # Проверка перехода к разделу «Булки»

    # Переход в соусы
    driver.find_element(*lc.SEC_SOUSES).click()

    # Прокрутка до последнего элемента в разделе булки
    elem1 = driver.find_element(*lc.MENU_ROLS)
    driver.execute_script("arguments[0].scrollIntoView();", elem1)

    # Проверка, что в атрибуте тега появился текст (кнопка "булки" выбрана)
    assert "tab_tab_type_current__2BEPc" in driver.find_element(*lc.ATTR_ROLLS).get_attribute('class')

def test_track_to_top(driver, login):  # Проверка перехода к разделу «Начинки»

    # Прокрутка до последнего элемента в разделе начинки
    elem1 = driver.find_element(*lc.MENU_TOP)
    driver.execute_script("arguments[0].scrollIntoView();", elem1)

    # Проверка, что в атрибуте тега появился текст (кнопка "начинки" выбрана)
    assert "tab_tab_type_current__2BEPc" in driver.find_element(*lc.ATTR_TOP).get_attribute('class')
