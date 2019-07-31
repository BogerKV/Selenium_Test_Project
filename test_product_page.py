from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.cart_page import CartPage
import time
import pytest

link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"

@pytest.mark.need_review
def test_guest_can_add_product_to_cart(browser):
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.should_be_add_to_basket_btn()   # присутствует кнопка добавления товара
    page.add_product_to_cart()  # добавление товара в корзину
 
@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.go_to_login_page()          # выполняем метод страницы - переходим на страницу логина    
    login_page = LoginPage(browser, browser.current_url) # инициализируем Page Object со страницей логина
    login_page.should_be_login_page() # проверка, что страница является страницей логина

@pytest.mark.need_review
def test_guest_cant_see_product_in_cart_opened_from_product_page(browser):
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()
    page.go_to_cart() # переход в корзину
    cart_page = CartPage(browser, browser.current_url) # инициализируем Page Object со страницей корзины
    cart_page.should_not_be_product_in_cart() # проверка, что в корзине нет товаров
    cart_page.should_be_cart_is_empty_message() # присутствует текст о том, что корзина пустая

def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.should_not_be_success_message()
    
def test_guest_cant_see_success_message_after_adding_product_to_cart(browser):
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.add_product()
    page.should_not_be_success_message()
    
def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link() # присутствует ссылка на страницу логина
        
def test_message_disappeared_after_adding_product_to_cart(browser):
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.add_product()
    page.should_be_disappeared_success_message()


class TestUserAddToCartFromProductPage(object):
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
        page.open()                      # открываем страницу
        page.go_to_login_page()          # выполняем метод страницы - переходим на страницу логина    
        login_page = LoginPage(browser, browser.current_url) # инициализируем Page Object со страницей логина
        email = "user_" + str(time.time()) + "@testmail.ru"
        password = "Strong_pass123"
        login_page.register_new_user(email, password)
        login_page.should_be_authorized_user()
        
    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
        page.open()                      # открываем страницу
        page.should_not_be_success_message()
    
    @pytest.mark.need_review
    def test_user_can_add_product_to_cart(self, browser):
        page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
        page.open()                      # открываем страницу
        page.should_be_add_to_basket_btn()            
        page.add_product_to_cart()
    