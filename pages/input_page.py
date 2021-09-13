from .base_page import BasePage
from .locators import LoginLocators, InputPageLocators, OkModal
from selenium.webdriver.support.ui import Select

class InputPage(BasePage):
    def should_be_input_page(self):
        self.should_be_email_input()
        self.should_be_name_input()
        self.should_be_sex_selection()
        self.should_be_checkboxes()
        self.should_be_radiobuttons()
        self.should_be_add_button()
        self.should_be_added_table()

    def should_be_email_input(self):
        assert self.is_element_present(*InputPageLocators.EMAIL_INPUT), "Email input is not presented"
        assert self.is_correct_msg(*InputPageLocators.EMAIL_INPUT_LABEL, InputPageLocators.EMAIL_INPUT_LABEL_TEXT), \
            f"Invalid label for email input, should be {InputPageLocators.EMAIL_INPUT_LABEL_TEXT}"

    def should_be_name_input(self):
        assert self.is_element_present(*InputPageLocators.NAME_INPUT), "Name input is not presented"
        assert self.is_correct_msg(*InputPageLocators.NAME_INPUT_LABEL, InputPageLocators.NAME_INPUT_LABEL_TEXT), \
            f"Invalid label for name input, should be {InputPageLocators.NAME_INPUT_LABEL_TEXT}"

    def should_be_sex_selection(self):
        assert self.is_element_present(*InputPageLocators.SEX_SELECT), "Sex selection input is not presented"
        assert self.is_correct_msg(*InputPageLocators.SEX_SELECTION_LABEL, InputPageLocators.SEX_SELECTION_LABEL_TEXT), \
            f"Invalid label for sex selection, should be {InputPageLocators.SEX_SELECTION_LABEL_TEXT}"
        options = self.get_elements(*InputPageLocators.SEX_OPTIONS)
        optionsCount = len(options)
        assert optionsCount == 2, f"Should be 2 sex options, but got {optionsCount}"
        for i in range(optionsCount):
            assert options[i].text == InputPageLocators.SEX_OPTION_TEXT[i], \
            f"Invalid label for #{i} option, should be {InputPageLocators.SEX_OPTION_TEXT[i]}"
        
    def should_be_checkboxes(self):
        checkboxCount = len(self.get_elements(*InputPageLocators.CHECKBOX))
        assert checkboxCount == 2, f"Should be 2 checkboxes, but got {checkboxCount}"
        checkboxNames = self.get_elements(*InputPageLocators.CHECKBOX_LABEL)
        for i in range(len(checkboxNames)):
            assert checkboxNames[i].text == InputPageLocators.CHECKBOX_VARIANTS[i], \
            f"Invalid label for checkbox #{i}, should be {InputPageLocators.CHECKBOX_VARIANTS[i]}"
        

    def should_be_radiobuttons(self):
        radioCount = len(self.get_elements(*InputPageLocators.RADIO))
        assert radioCount == 3, f"Should be 3 radiobuttons, but got {radioCount}"
        radioNames = self.get_elements(*InputPageLocators.RADIO_LABLE)
        for i in range(len(radioNames)):
            assert radioNames[i].text == InputPageLocators.RADIO_VARIANTS[i], \
            f"Invalid label for radio #{i}, should be {InputPageLocators.RADIO_VARIANTS[i]}"
        

    def should_be_add_button(self):
        assert self.is_element_present(*InputPageLocators.ADD_BUTTON), "'Add' button is not presented"
        assert self.is_correct_msg(*InputPageLocators.ADD_BUTTON, InputPageLocators.ADD_BUTTON_TEXT), \
            f"Invalid text in 'add' button, should be {InputPageLocators.ADD_BUTTON_TEXT}"


    def should_be_added_table(self):
        assert self.is_element_present(*InputPageLocators.ADDED_DATA_TABLE), "Table for added data is not presented"
        columns = self.get_elements(*InputPageLocators.ADDED_TABLE_HEADER)
        assert len(columns) == 5, f"Should be 5 columns, but got {len(columns)}"
        for i in range(len(columns)):
            assert columns[i].text == InputPageLocators.COLUMNS[i], f"Invalid column name, should be {InputPageLocators.COLUMNS[i]}"

    def should_be_email_error(self):
        self.decrease_added_count()
        assert self.is_element_present(*LoginLocators.EMAIL_ERROR), "Email error message is not presented"
        assert self.is_correct_msg(*LoginLocators.EMAIL_ERROR, LoginLocators.EMAIL_ERROR_MSG), \
            f"Invalid email error message, should be {LoginLocators.EMAIL_ERROR_MSG}"

    def should_be_name_error(self):
        self.decrease_added_count()
        assert self.is_element_present(*InputPageLocators.NAME_ERROR), \
            "Invalid name error message is not presented"
        assert self.is_correct_msg(*InputPageLocators.NAME_ERROR, InputPageLocators.NAME_ERROR_MSG), \
            f"Invalid name error message, should be {InputPageLocators.NAME_ERROR_MSG}"

    def fill_data(self, email, name, sex, check1, check2, radio):
        email_input = self.browser.find_element(*InputPageLocators.EMAIL_INPUT)
        email_input.send_keys(email)

        name_input = self.browser.find_element(*InputPageLocators.NAME_INPUT)
        name_input.send_keys(name)

        sex_selection= Select(self.browser.find_element_by_xpath((InputPageLocators.SEX_SELECT)[1]))
        if (sex == 'w'):
            sex_selection.select_by_visible_text('Женский')
        else: 
            sex_selection.select_by_visible_text('Мужской')
        
        if (check1):
            self.click_on_element(*InputPageLocators.CHECKBOX,"[1]")
        if (check2):
            self.click_on_element(*InputPageLocators.CHECKBOX,"[2]")

        if (radio == "1"):
            self.click_on_element(*InputPageLocators.RADIO, "[1]")
        elif (radio == "2"):
            self.click_on_element(*InputPageLocators.RADIO, "[2]")
        elif (radio == "3"):
            self.click_on_element(*InputPageLocators.RADIO, "[3]")

    def uncheck_checkbox(self, how, what, numBox):
        checkbox = self.browser.find_element(how, "(" + what + ")" + numBox)
        if (checkbox.get_attribute('checked') == 'true'):
            checkbox.click()

    def clear_radio(self, how, what, numBox):
        radio = self.browser.find_element(how, "(" + what + ")" + numBox)
        if (radio.get_attribute('checked') != None):
            self.browser.execute_script("arguments[0].removeAttr('checked')", radio)


    def clear_all_fields(self):
        email_input = self.browser.find_element(*InputPageLocators.EMAIL_INPUT)
        email_input.clear()

        name_input = self.browser.find_element(*InputPageLocators.NAME_INPUT)
        name_input.clear()
        
        self.uncheck_checkbox(*InputPageLocators.CHECKBOX,"[1]")
        self.uncheck_checkbox(*InputPageLocators.CHECKBOX,"[2]")
        
        self.clear_radio(*InputPageLocators.RADIO, "[1]")
        self.clear_radio(*InputPageLocators.RADIO, "[2]")
        self.clear_radio(*InputPageLocators.RADIO, "[3]")


    def should_be_invalid_email_password_error(self):
        assert self.is_element_present(*LoginLocators.INVALID_ERROR), \
            "Invalid email/password error message is not presented"
        assert self.is_correct_msg(*LoginLocators.INVALID_ERROR, LoginLocators.INVALID_MSG), \
            f"Invalid email/password error message, should be {LoginLocators.INVALID_MSG}"

    def add_inputed_data(self):
        self.add_to_added_count()
        add_btn = self.browser.find_element(*InputPageLocators.ADD_BUTTON)
        add_btn.click()

    def should_be_correct_columns_data(self, columns, email, name, sex, check1, check2, radio):
        assert columns[0].text == email, \
            f"Invalid email was added to the table, should be {email}, but got {columns[0].text}"
        assert columns[1].text == name, \
            f"Invalid name was added to the table, should be {name},, but got {columns[1].text}"
        if (sex == "w"):
            text = "Женский"
        else: 
            text = 'Мужской'
        assert columns[2].text == text, \
            f"Invalid sex was added to the table, should be {text}, but got {columns[2].text}"

        if (check1 and check2):
            text = "1.1, 1.2"
        elif check1:
            text = "1.1"
        elif check2:
            text = "1.2"
        else: 
            text = "Нет"
        assert columns[3].text == text, \
            f"Invalid checkbox was added to the table, should be {text}, but got {columns[3].text}"

        if (radio == "1"):
            text = "2.1"
        elif (radio == "2"):
            text = "2.2"
        elif (radio == "3"):
            text = "2.3"
        else: 
            text = ""
        assert columns[4].text == text, \
            f"Invalid radio was added to the table, should be {text}, but got {columns[4].text}"


    def data_should_be_added_to_table(self, email, name, sex, check1, check2, radio):
        rows = self.get_elements(*InputPageLocators.ADDED_DATA_ROW)
        
        assert len(rows) == self.get_added_count(), \
            f"Data wasn't added to table, should be {self.get_added_count()}, but got {len(rows)}"
        columns = self.get_columns_from_row(*InputPageLocators.ADDED_DATA_ROW, len(rows))
        self.should_be_correct_columns_data(columns, email, name, sex, check1, check2, radio)
        
    def all_data_should_be_added_to_table(self, inputedArray):
        rows = self.get_elements(*InputPageLocators.ADDED_DATA_ROW)
        assert len(rows) == self.get_added_count(), \
            f"Added data count isn't equal actual, should be {self.get_added_count()}, but got {len(rows)}"
        
        for i in range(len(rows)):
            columns = self.get_columns_from_row(*InputPageLocators.ADDED_DATA_ROW, i+1)
            assert len(columns) == 5, f"should be 5 columns, but got {len(columns)}"
            self.should_be_correct_columns_data(columns, *inputedArray[i])


    def should_be_modal_ok_message(self):
        assert self.is_element_present(*OkModal.MODAL), "Modal window with ok message is not presented"
        assert self.is_correct_msg(*OkModal.MODAL_CONTENT, OkModal.MODAL_CONTENT_TEXT), \
            f"Invalid text in modal window, should be {OkModal.MODAL_CONTENT_TEXT}"
        assert self.is_element_present(*OkModal.OK_BTN), "Ok button in modal is not presented"

    def close_modal(self):
        self.click_on_element(*OkModal.OK_BTN, "")
        assert self.is_disappeared(*OkModal.MODAL), "Modal isn't closed, but should be"

    def login_user(self, email, password):
        email_input = self.browser.find_element(*LoginLocators.EMAIL_INPUT)
        email_input.send_keys(email)

        password_input = self.browser.find_element(*LoginLocators.PASSWORD_INPUT)
        password_input.send_keys(password)

        login_btn = self.browser.find_element(*LoginLocators.LOGIN_BTN)
        login_btn.click()

    def should_not_be_input_error_msgs(self):
        assert self.is_not_element_present(*LoginLocators.EMAIL_ERROR), "There's email error with valid input"
        assert self.is_not_element_present(*InputPageLocators.NAME_ERROR), "There's name error with valid input"
