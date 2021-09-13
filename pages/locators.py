from selenium.webdriver.common.by import By

class LoginLocators():
    LOGIN_LINK = "qa-test.html"
    EMAIL = "test@protei.ru"
    PASSWORD = "test"
    EMAIL_INPUT = (By.XPATH, "//input[@id='loginEmail']")
    PASSWORD_INPUT = (By.XPATH, "//input[@id='loginPassword']")
    LOGIN_BTN = (By.XPATH, "//button[@id='authButton']")
    LOGIN_BTN_TEXT = "Вход"
    EMAIL_ERROR = (By.XPATH, "//div[@id='emailFormatError']")
    INVALID_ERROR = (By.XPATH, "//div[@id='invalidEmailPassword']")
    INVALID_MSG = "Неверный E-Mail или пароль"
    EMAIL_ERROR_MSG = "Неверный формат E-Mail"
    EMAIL_LABEL = (By.XPATH, "//label[@for='loginEmail']")
    EMAIL_LABLE_TEXT = "E-Mail:"
    PASSWORD_LABEL = (By.XPATH, "//label[@for='loginPassword']")
    PASSWORD_LABLE_TEXT = "Пароль:"
    CLOSE_ERROR = (By.XPATH, "//a[contains(@class,'close')]")

class InputPageLocators():
    INPUT_PAGE = (By.XPATH, "//div[@id='inputsPage']")
    EMAIL_INPUT = (By.XPATH, "//input[@id='dataEmail']")
    EMAIL_INPUT_LABEL = (By.XPATH, "//label[@for='dataEmail']")
    EMAIL_INPUT_LABEL_TEXT = "E-Mail:"
    NAME_INPUT = (By.XPATH, "//input[@id='dataName']")
    NAME_INPUT_LABEL = (By.XPATH, "//label[@for='dataName']")
    NAME_INPUT_LABEL_TEXT = "Имя:"
    SEX_SELECT = (By.XPATH, "//select[@id='dataGender']")
    SEX_SELECTION_LABEL = (By.XPATH, "//label[@for='dataGender']")
    SEX_SELECTION_LABEL_TEXT = "Пол:"
    SEX_OPTIONS = (By.XPATH, "//select[@id='dataGender']/option")
    SEX_OPTION_TEXT = ["Мужской", "Женский"]
    CHECKBOX = (By.XPATH, "//input[@type='checkbox']")
    CHECKBOX_VARIANTS = ["Вариант 1.1", "Вариант 1.2"]
    CHECKBOX_LABEL = (By.XPATH, "//input[@type='checkbox']/ancestor::div[1]")
    RADIO = (By.XPATH, "//input[@type='radio']")
    RADIO_LABLE = (By.XPATH, "//input[@type='radio']/ancestor::div[1]")
    RADIO_VARIANTS = ["Вариант 2.1", "Вариант 2.2", "Вариант 2.3"]
    ADD_BUTTON = (By.XPATH, "//button[@id='dataSend']")
    ADD_BUTTON_TEXT = "Добавить"
    ADDED_DATA_TABLE = (By.XPATH, "//table[@id='dataTable']")
    ADDED_TABLE_HEADER = (By.XPATH, "//table[@id='dataTable']//tr[1]/th")
    ADDED_DATA_ROW = (By.XPATH, "//table[@id='dataTable']/tbody/tr")
    CELL = (By.XPATH, "/td")
    COLUMNS = ["E-Mail", "Имя", "Пол", "Выбор 1", "Выбор 2"]
    NO_SELECTION = "Нет"
    NAME_ERROR = (By.XPATH, "//div[@id='blankNameError']")
    NAME_ERROR_MSG = "Поле имя не может быть пустым"

class OkModal():
    MODAL = (By.XPATH, "//div[@class='uk-modal-dialog']")
    MODAL_CONTENT = (By.XPATH, "//div[@class='uk-margin uk-modal-content']")
    MODAL_CONTENT_TEXT = "Данные добавлены."
    OK_BTN = (By.XPATH, "//button[contains(@class,'uk-modal-close')]")
    OK_BTN_TEXT = "Ok"


