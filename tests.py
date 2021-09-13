from pages.login_page import LoginPage
from pages.input_page import InputPage
from selenium.webdriver.common.by import By
import pytest
from pathlib import Path

link = (str)(Path().absolute()) + "\\" + "qa-test.html"
str_256 = "bABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghigklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghigklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ@ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghigklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghigklmnopqrstuvwxyzabcdefghigklmnopqrst"
str_257 = "bABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghigklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghigklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ@ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghigklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghigklmnopqrstuvwxyzabcdefghigklmnopqrstP"

sql_pwd = "SELECT * FROM users WHERE email = 'test@protei.ru' OR 1 = 1 LIMIT 1 — ' ] AND password ='test';"

email_OK  = "test@protei.ru"
password_OK = "test"
correct_inputed_data = [("peter@mail.ru","Peter", 'm', 0, 0, 3), \
    ("mary@gmail.com","Mary", 'w', 1, 1, ""), \
    ("charlie@bk.ru","Charlie", "", 1, 0, 1)]

@pytest.mark.login_tests
class TestLogin():

    # Login page loads successfully
    def test_valid_login_page(self, browser):
        page = LoginPage(browser, link)  
        page.open()                    
        page.should_be_login_page()

    # Successfull login with right email and password
    def test_valid_login_data(self, browser):
        page = LoginPage(browser, link) 
        page.open()             
        page.should_be_login_page()
        page.login_user("test@protei.ru", "test")
        page.should_not_be_login_error_msgs()
        inputpage = InputPage(browser, browser.current_url)
        inputpage.should_be_input_page()

    # "Неверный E-Mail или пароль" Error message are shown with incorrect email
    def test_login_incorrect_email(self, browser):
        page = LoginPage(browser, link) 
        page.open()             
        page.should_be_login_page()
        page.login_user("invalidtest@protei.ru", "test")
        page.should_be_invalid_email_password_error()
        page.close_error_message()
        page.should_not_be_login_error_msgs()

    # "Неверный E-Mail или пароль" Error message are shown with incorrect password
    def test_login_incorrect_password(self, browser):
        page = LoginPage(browser, link) 
        page.open()             
        page.should_be_login_page()
        page.login_user("test@protei.ru", "invalidtest")
        page.should_be_invalid_email_password_error()
        page.close_error_message()
        page.should_not_be_login_error_msgs()

    # "Неверный E-Mail или пароль" Error message are shown with incorrect email & password
    def test_login_incorrect_email_password(self, browser):
        page = LoginPage(browser, link) 
        page.open()             
        page.should_be_login_page()
        page.login_user("incorrecttest@protei.ru", "invalidtest")
        page.should_be_invalid_email_password_error()
        page.close_error_message()
        page.should_not_be_login_error_msgs()

    # "Неверный формат E-Mail" Error message are shown with empty fields
    def test_login_empty_data(self, browser):
        page = LoginPage(browser, link) 
        page.open()             
        page.should_be_login_page()
        page.login_user("", "")
        page.should_be_email_error()
        page.close_error_message()
        page.should_not_be_login_error_msgs()

    # "Неверный формат E-Mail" Error message are shown with invalid email
    @pytest.mark.xfail
    @pytest.mark.parametrize('email',["myemail", "@", "@domen", "myemail@", "123@123", \
                            "", "w@w", "_@_", "^@^", "?@?", ".@.", "test@test@test" \
                            "   ", " test@protei.ru ", "test @protei.ru"])
    def test_login_invalid_email(self, browser, email):
        page = LoginPage(browser, link) 
        page.open()             
        page.should_be_login_page()
        page.login_user(email, "test")
        page.should_be_email_error()
        page.close_error_message()
        page.should_not_be_login_error_msgs()

    # "Неверный E-Mail или пароль" Error message are shown with invalid password
    @pytest.mark.parametrize('password',["", "@", "@123", "^^", "testtesttest", \
                            "   ", sql_pwd, " test ", "test@protei.ru"])
    def test_login_invalid_password(self, browser, password):
        page = LoginPage(browser, link) 
        page.open()             
        page.should_be_login_page()
        page.login_user("test@protei.ru", password)
        page.should_be_invalid_email_password_error()
        page.close_error_message()
        page.should_not_be_login_error_msgs()

    # "Неверный E-Mail или пароль" Error message are shown with email (255 length)
    def test_login_incorrect_email_256(self, browser):
        page = LoginPage(browser, link) 
        page.open()             
        page.should_be_login_page()
        page.login_user(str_256, "invalidtest")
        page.should_be_invalid_email_password_error()
        page.close_error_message()
        page.should_not_be_login_error_msgs()

    # "Неверный формат E-Mail" Error message are shown with email (256 length)
    @pytest.mark.xfail
    def test_login_incorrect_email_257(self, browser):
        page = LoginPage(browser, link) 
        page.open()             
        page.should_be_login_page()
        page.login_user(str_257, "invalidtest")
        page.should_be_invalid_email_password_error()
        page.close_error_message()
        page.should_not_be_login_error_msgs()


@pytest.mark.input_tests
class TestInput():

    # Input page loads successfully
    def test_valid_input_page(self, browser):
        page = LoginPage(browser, link) 
        page.open()             
        page.should_be_login_page()
        page.login_user(email_OK, password_OK)
        page.should_not_be_login_error_msgs()
        inputpage = InputPage(browser, browser.current_url)
        inputpage.should_be_input_page()

    # Data successfully added with filling all inputs with valid values
    @pytest.mark.parametrize('inputed_data',[(email_OK,"Peter", 'w', 0, 1, 2), (email_OK,"Peter", 'm', 1, 1, ""), \
    (email_OK,"Peter", 'w', 0, 0, 2), (email_OK,"Peter", "", 0, 0, "")])
    def test_input_correct_data(self, browser, inputed_data):
        page = LoginPage(browser, link) 
        page.open()             
        page.should_be_login_page()
        page.login_user(email_OK, password_OK)
        page.should_not_be_login_error_msgs()
        inputpage = InputPage(browser, browser.current_url)
        inputpage.should_be_input_page()
        inputpage.fill_data(*inputed_data)
        inputpage.add_inputed_data()
        inputpage.should_not_be_login_error_msgs()
        inputpage.should_be_modal_ok_message()
        inputpage.close_modal()
        inputpage.data_should_be_added_to_table(*inputed_data)

    # "Неверный формат E-Mail" Error message are shown with empty fields
    def test_input_empty_data(self,browser):
        page = LoginPage(browser, link) 
        page.open()             
        page.should_be_login_page()
        page.login_user(email_OK, password_OK)
        page.should_not_be_login_error_msgs()
        inputpage = InputPage(browser, browser.current_url)
        inputpage.should_be_input_page()
        inputpage.fill_data("", "", "", 0, 0, "")
        inputpage.add_inputed_data()
        inputpage.should_be_email_error()
        
    # "Поле имя не может быть пустым" Error message are shown with empty name
    def test_input_empty_name(self,browser):
        page = LoginPage(browser, link)
        page.open()             
        page.should_be_login_page()
        page.login_user(email_OK, password_OK)
        page.should_not_be_login_error_msgs()
        inputpage = InputPage(browser, browser.current_url)
        inputpage.should_be_input_page()
        inputpage.fill_data(email_OK, "", "", 0, 0, "")
        inputpage.add_inputed_data()
        inputpage.should_be_name_error()

    # "Неверный формат E-Mail" Error message are shown with empty email
    def test_input_empty_email(self,browser):
        page = LoginPage(browser, link)
        page.open()             
        page.should_be_login_page()
        page.login_user(email_OK, password_OK)
        page.should_not_be_login_error_msgs()
        inputpage = InputPage(browser, browser.current_url)
        inputpage.should_be_input_page()
        inputpage.fill_data("", "testUser", "", 0, 0, "")
        inputpage.add_inputed_data()
        inputpage.should_be_email_error()

    # Error message can be closed
    def test_close_error_message(self,browser):
        page = LoginPage(browser, link)
        page.open()             
        page.should_be_login_page()
        page.login_user(email_OK, password_OK)
        page.should_not_be_login_error_msgs()
        inputpage = InputPage(browser, browser.current_url)
        inputpage.should_be_input_page()
        inputpage.fill_data("", "testUser", "", 0, 0, "")
        inputpage.add_inputed_data()
        inputpage.should_be_email_error()
        inputpage.close_error_message()
        inputpage.should_not_be_input_error_msgs()

    # Several correct data added successfully
    def test_input_correct_several_data(self, browser):
        page = LoginPage(browser, link) 
        page.open()             
        page.should_be_login_page()
        page.login_user(email_OK, password_OK)
        page.should_not_be_login_error_msgs()
        inputpage = InputPage(browser, browser.current_url)
        inputpage.should_be_input_page()
        for input_D in correct_inputed_data:
            inputpage.fill_data(*input_D)
            inputpage.add_inputed_data()
            inputpage.should_not_be_login_error_msgs()
            inputpage.should_be_modal_ok_message()
            inputpage.close_modal()
            inputpage.clear_all_fields()
        inputpage.all_data_should_be_added_to_table(correct_inputed_data)

    # "Неверный формат E-Mail" Error message are shown with invalid email
    @pytest.mark.xfail
    @pytest.mark.parametrize('email',["myemail", "@", "@domen", "myemail@", "123@123", \
                        "", "w@w", "_@_", "^@^", "?@?", ".@.", "test@test@test" \
                        "   ", " test@protei.ru ", "test @protei.ru"])
    def test_input_incorrect_email(self, browser, email):
        page = LoginPage(browser, link) 
        input_data = (email, "Peter", "m", 0, 0, 3)
        page.open()             
        page.should_be_login_page()
        page.login_user(email_OK, password_OK)
        page.should_not_be_login_error_msgs()
        inputpage = InputPage(browser, browser.current_url)
        inputpage.should_be_input_page()
        inputpage.fill_data(*input_data)
        inputpage.add_inputed_data()
        inputpage.should_be_email_error()
        inputpage.close_error_message()
        inputpage.should_not_be_input_error_msgs()

    # Error message are shown with invalid name
    @pytest.mark.xfail
    @pytest.mark.parametrize('name',["", "123", "_", "^", "?", ".", " "])
    def test_input_incorrect_name(self, browser, name):
        page = LoginPage(browser, link) 
        page.open()   
        input_data = ("test@protei.ru", name, "m", 0, 0, 3)          
        page.should_be_login_page()
        page.login_user(email_OK, password_OK)
        page.should_not_be_login_error_msgs()
        inputpage = InputPage(browser, browser.current_url)
        inputpage.should_be_input_page()
        inputpage.fill_data(*input_data)
        inputpage.add_inputed_data()
        inputpage.should_be_name_error()
        inputpage.close_error_message()
        inputpage.should_not_be_input_error_msgs()

    # Data successfully added with name (256 length)
    def test_input_256_name(self, browser):
        page = LoginPage(browser, link) 
        page.open()             
        page.should_be_login_page()
        page.login_user(email_OK, password_OK)
        page.should_not_be_login_error_msgs()
        inputpage = InputPage(browser, browser.current_url)
        inputpage.should_be_input_page()
        inputpage.fill_data(email_OK, str_256, "", 0, 0, "")
        inputpage.add_inputed_data()
        inputpage.should_not_be_input_error_msgs()
        inputpage.should_be_modal_ok_message()
        inputpage.close_modal()
        inputpage.data_should_be_added_to_table(email_OK, str_256, "", 0, 0, "")

    # Error message is shown while trying to add data with name (257 length)
    def test_input_257_name(self, browser):
        page = LoginPage(browser, link) 
        page.open()             
        page.should_be_login_page()
        page.login_user(email_OK, password_OK)
        page.should_not_be_login_error_msgs()
        inputpage = InputPage(browser, browser.current_url)
        inputpage.should_be_input_page()
        inputpage.fill_data(email_OK, str_257, "", 0, 0, "")
        inputpage.add_inputed_data()
        inputpage.should_be_name_error()