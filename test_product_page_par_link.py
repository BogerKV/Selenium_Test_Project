from .pages.product_page import ProductPage
import time
import pytest

@pytest.mark.parametrize('link', [
                                 "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                 "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                 "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                 "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                 "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                 "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                 "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                 "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                 "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                 "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"
                                ]
                        )
                        
def test_guest_can_add_product_to_cart(browser, link):
    # link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    #link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.should_be_add_to_basket_btn()          # выполняем метод страницы - переходим на страницу логина    
    page.add_product_to_cart()
 