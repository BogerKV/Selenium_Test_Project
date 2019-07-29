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
       
class ProductPageLocators(object):
    ADD_BTN = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRICE = (By.CSS_SELECTOR, ".product_main p.price_color")
    PRICE_AFTER_ADD = (By.XPATH, "//p[contains(text(),'Your basket total')]/strong")
    SUCCESS_MESSAGE = (By.XPATH, "//div[contains(@class, 'alert-success')]")
    
class BasePageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")