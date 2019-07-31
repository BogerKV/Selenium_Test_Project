from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def register_new_user(self, email, password):
        # поиск элементов формы регистрации пользователя
        reg_email = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL)
        reg_pass1 = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD1)
        reg_pass2 = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD2)
        reg_button = self.browser.find_element(*LoginPageLocators.REGISTRATION_BTN)
        
        # заполнение полей и нажатие на "Register"
        reg_email.send_keys(email)
        reg_pass1.send_keys(password)
        reg_pass2.send_keys(password)
        reg_button.click()
    
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # проверка на корректный url адрес
        assert self.browser.current_url.find(LoginPageLocators.LOGIN_SUBSTR)!=-1, "Login URL does not contain \"login\" "
        

    def should_be_login_form(self):
        # проверка, что есть форма логина на странице
        assert (self.is_element_present(*LoginPageLocators.LOGIN_FORM) 
            and self.is_element_present(*LoginPageLocators.LOGIN_USER)
            and self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD)
            and self.is_element_present(*LoginPageLocators.LOGIN_BTN)
            ), "Login form is not presented"    

    def should_be_register_form(self):
        # проверка, что есть форма регистрации на странице
        assert (self.is_element_present(*LoginPageLocators.REGISTER_FORM)
            and self.is_element_present(*LoginPageLocators.REGISTRATION_EMAIL)
            and self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD1)
            and self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD2)
            and self.is_element_present(*LoginPageLocators.REGISTRATION_BTN)
            ), "Register form is not presented"