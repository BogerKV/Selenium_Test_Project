from .base_page import BasePage
from .locators import ProductPageLocators
import time
from selenium.webdriver.common.by import By
import re

class ProductPage(BasePage):
    def add_product_to_cart(self):
        product_name = self.add_product()
        self.should_be_message_about_add_product_success(product_name)
        self.should_be_message_with_price_of_added_product()
        
    def should_be_add_to_basket_btn(self):
        assert self.is_element_present(*ProductPageLocators.ADD_BTN), "Add to basket button is not presented"
        
    def should_be_message_about_add_product_success(self, product):
        Div_text = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE).text
        assert (
                Div_text.find(product+" has been added to your basket")!=-1
                ), "No message!!! URL: "+self.url
        
    def should_be_message_with_price_of_added_product(self):
        price = self.get_price_before_add() 
        price_after_add = self.get_price_after_add()
        assert price_after_add == price, "Wrong price in the message after product adding!"
    
    def get_price_before_add(self):
        price_text = self.browser.find_element(*ProductPageLocators.PRICE).text
        price = re.findall(r"[-+]?\d*\.\d+|\d+", price_text)[0]
        return price
        
    def get_price_after_add(self):
        price_after_add_text = self.browser.find_element(*ProductPageLocators.PRICE_AFTER_ADD).text
        price_after_add = re.findall(r"[-+]?\d*\.\d+|\d+", price_after_add_text)[0]
        return price_after_add
    
    def add_product(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        add_button = self.browser.find_element(*ProductPageLocators.ADD_BTN)
        add_button.click()
        self.solve_quiz_and_get_code()
        return product_name
    
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
        "Success message is presented, but should not be"    
        
    def should_be_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
        "Success message is presented, but should be disappeared"
    