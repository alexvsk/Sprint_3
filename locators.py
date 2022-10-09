from selenium.webdriver.common.by import By


class Locators:
    NAME_REG = (By.XPATH, ".//label[text()='Имя']/parent::div/input")  # Поле "Имя" в форме регистрации
    EMAIL_REG = (By.XPATH, ".//label[text()='Email']/parent::div/input")  # Поле "Email" в форме регистрации
    PASS_REG = (By.XPATH, ".//label[text()='Пароль']/parent::div/input")  # Поле "Пароль" в форме регистрации
    BUTTON_REG = (By.XPATH, ".//button[text()='Зарегистрироваться']")  # Кнопка "Зарегистрироваться" на форме регистрации
    LOGIN_FORM = (By.CLASS_NAME, "Auth_login__3hAey")  # Отображение формы входа
    PASS_ERR = (By.XPATH, ".//div[@class = 'input pr-6 pl-6 input_type_password input_size_default input_status_error']")  # Отображение ошибки поля ввода
    PASS_ERR_TEXT = (By.XPATH, ".//p[@class = 'input__error text_type_main-default']")  # Текст ошибки ввода
    BUTTON_LOG_MAIN = (By.CSS_SELECTOR, ".button_button__33qZ0") # Кнопка "Войти"/"Оформить заказ" на главной
    EMAIL_LOG = (By.XPATH, ".//label[text()='Email']/parent::div/input")  # Поле "Email" в форме авторизации
    PASS_LOG = (By.XPATH, ".//label[text()='Пароль']/parent::div/input")  # Поле "Пароль" в форме авторизации
    BUTTON_LOG = (By.XPATH, ".//button[text()='Войти']")  # Кнопка "Войти" в форме авторизации
    MENU_MAIN = (By.CLASS_NAME, "BurgerIngredients_ingredients__1N8v2")  # Отображение меню с ингридиентами на главной
    BUTTON_ACCOUNT = (By.XPATH, ".//a[@href='/account'][last()]")  # Кнопка "Личный кабинет" на главной
    BUTTON_REG1 = (By.XPATH, ".//a[@href='/register'][last()]")  # Кнопка "Зарегистрироваться" в ЛК
    BUTTON_LOG1 = (By.XPATH, ".//a[@href='/login'][last()]")  # Кнопка "Войти" на странице регистрации
    BUTTON_PASS_FORGOT = (By.XPATH, ".//a[@href='/forgot-password'][last()]")  # Кнопка "Восстановить пароль" в форме входа
    ACCOUNT_TEXT = (By.XPATH, ".//p[@class='Account_text__fZAIn text text_type_main-default']")  #  Текст в ЛК "В этом разделе вы можете изменить свои персональные данные"
    BUTTON_LOGOUT = (By.XPATH, ".//button[@type='button'][last()]")   # Кнопка "Выйти" в ЛК
    BUTTON_CONST = (By.XPATH, ".//p[text()='Конструктор'][last()]")  #  Кнопка "Конструктор"
    MAIN_TEXT = (By.XPATH, ".//section[@class='BurgerIngredients_ingredients__1N8v2']/h1")  # Заголовок "Соберите бургер" на главной
    LOGO = (By.XPATH, ".//a[@href='/'][last()]")  # Логотип Stellar Burgers
    SEC_SOUSES = (By.XPATH, ".//span[text()='Соусы']")  # Раздел соусы
    MENU_SOUSES = (By.XPATH, ".//img[@alt='Соус с шипами Антарианского плоскоходца']")  # Последний ингридент в меню соусов
    MENU_ROLS = (By.XPATH, ".//img[@alt='Краторная булка N-200i']")  # Последний ингридент в меню булок
    MENU_TOP = (By.XPATH, ".//img[@alt='Сыр с астероидной плесенью']")  # Последний ингридент в меню начинок
    ATTR_SOUSES = (By.XPATH, ".//span[text()='Соусы']/parent::div")  # Родительский тег для соусов
    ATTR_ROLLS = (By.XPATH, ".//span[text()='Булки']/parent::div")  # Родительский тег для булок
    ATTR_TOP = (By.XPATH, ".//span[text()='Начинки']/parent::div")  # Родительский тег для начинок







