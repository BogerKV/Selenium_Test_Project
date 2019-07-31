from .base_page import BasePage
from .locators import CartPageLocators
import time


class CartPage(BasePage):
    def should_not_be_product_in_cart(self):
        # проверка, что в корзине отсутствуют товары
        assert self.is_not_element_present(*CartPageLocators.BASKET_ITEMS), \
        "Cart is not empry!"

    def should_be_cart_is_empty_message(self):
        # проверка на наличие сообщения о том, что корзина пуста
        assert self.is_element_present(*CartPageLocators.CART_IS_EMPTY_MES), \
        "Message that cart is empty is not presented, but should be"