from .base_page import BasePage
from .locators import InputPageLocators, LoginLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_email_input()
        self.should_be_password_input()
        self.should_be_log_in_btn()

    def should_be_email_input(self):
        assert self.is_element_present(*LoginLocators.EMAIL_INPUT), "Email input is not presented"
        assert self.is_correct_msg(*LoginLocators.EMAIL_LABEL, LoginLocators.EMAIL_LABLE_TEXT), \
            f"Invalid label for email input, should be {LoginLocators.EMAIL_LABLE_TEXT}"

    def should_be_password_input(self):
        assert self.is_element_present(*LoginLocators.PASSWORD_INPUT), "Password input is not presented"
        assert self.is_correct_msg(*LoginLocators.PASSWORD_LABEL, LoginLocators.PASSWORD_LABLE_TEXT), \
            f"Invalid label for password input, should be {LoginLocators.PASSWORD_LABLE_TEXT}"

    def should_be_log_in_btn(self):
        assert self.is_element_present(*LoginLocators.LOGIN_BTN), "'Log in' button is not presented"
        assert self.is_correct_msg(*LoginLocators.LOGIN_BTN, LoginLocators.LOGIN_BTN_TEXT), \
            f"Invalid text in 'log in' button, should be {LoginLocators.LOGIN_BTN_TEXT}"

    def should_be_email_error(self):
        assert self.is_element_present(*LoginLocators.EMAIL_ERROR), "Email error message is not presented"
        assert self.is_correct_msg(*LoginLocators.EMAIL_ERROR, LoginLocators.EMAIL_ERROR_MSG), \
            f"Invalid email error message, should be {LoginLocators.EMAIL_ERROR_MSG}"
        assert self.is_element_present(*LoginLocators.CLOSE_ERROR), "Close error button is not presented"

    def should_be_invalid_email_password_error(self):
        assert self.is_element_present(*LoginLocators.INVALID_ERROR), \
            "Invalid email/password error message is not presented"
        assert self.is_correct_msg(*LoginLocators.INVALID_ERROR, LoginLocators.INVALID_MSG), \
            f"Invalid email/password error message, should be {LoginLocators.INVALID_MSG}"
        assert self.is_element_present(*LoginLocators.CLOSE_ERROR), "Close error button is not presented"


    def login_user(self, email, password):
        email_input = self.browser.find_element(*LoginLocators.EMAIL_INPUT)
        email_input.send_keys(email)

        password_input = self.browser.find_element(*LoginLocators.PASSWORD_INPUT)
        password_input.send_keys(password)

        login_btn = self.browser.find_element(*LoginLocators.LOGIN_BTN)
        login_btn.click()

    
