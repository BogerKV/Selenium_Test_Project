from selenium.webdriver.common.by import By


class MainPageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#registration_link")
    
class LoginPageLocators(object):
    LOGIN_SUBSTR = "login"
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    LOGIN_USER = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "#id_login-password")
    LOGIN_BTN = (By.CSS_SELECTOR, "[name='login_submit']")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTRATION_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATION_PASSWORD1 = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTRATION_PASSWORD2 = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTRATION_BTN = (By.CSS_SELECTOR, "[name='registration_submit']")
       
    
    