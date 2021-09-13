from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException # в начале файла
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import LoginLocators
from selenium.webdriver.common.by import By
import math
import time


class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.addedCount = 0

    def get_added_count(self):
        return self.addedCount

    def decrease_added_count(self, ):
        self.addedCount -= 1

    def add_to_added_count(self):
        self.addedCount += 1

    def open(self):
        self.browser.get(self.url)

    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def go_to_basket_page(self):
        link = self.browser.find_element(*BasePageLocators.BTN_BASKET)
        link.click()

    def should_be_basket_link(self):
        assert self.is_element_present(*BasePageLocators.BTN_BASKET), "Basket link is not presented"

    def is_correct_msg(self, how, what, text):
        if (self.browser.find_element(how, what).text == text):
            return True
        print(self.browser.find_element(how, what).text)
        return False

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    def is_element_checked(self, how, what, opt):
        try:
            checkBox = self.browser.find_element(how, what + opt)
        except (NoSuchElementException):
            return False
        return checkBox.is_selected()

    def get_elements(self, how, what):
        return self.browser.find_elements(how, what)

    def get_columns_from_row(self, how, what, row):
        return self.browser.find_elements(how, what + "[" + (str)(row) + "]/td")

    def click_on_element(self, how, what, opt):
        self.browser.find_element(how,'(' + what + ')' + opt).click()
        return
        
    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).\
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True

    def close_error_message(self):
        self.click_on_element(*LoginLocators.CLOSE_ERROR,"")
        assert self.is_disappeared(*LoginLocators.CLOSE_ERROR), \
            f"Error message should be disappeared"

    def should_not_be_login_error_msgs(self):

        assert self.is_not_element_present(*LoginLocators.EMAIL_ERROR), "There's email error with valid input"
        assert self.is_not_element_present(*LoginLocators.INVALID_ERROR), "There's invalid data error with valid input"
