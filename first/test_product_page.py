import pytest
import time
import math
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                   pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def ttest_guest_can_add_product_to_basket(browser, link):
    product_page = ProductPage(browser, link)                      # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    product_page.open()                                            # выполняем метод "open" из base_page.py
    product_page.add_product_to_basket()                           # выполнили метод add_product_to_basket из файла product_page.py
    product_page.solve_quiz_and_get_code()                         # решаем пример и вводим ответ
    product_page.should_be_success_message_about_add_product_to_basket_with_product_name()
    product_page.should_total_price_in_basket_equal_product_price()

def ttest_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    product_page = ProductPage(browser, link)         # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    product_page.open()                               # выполняем метод "open" из base_page.py
    product_page.add_product_to_basket()              # выполнили метод add_product_to_basket из файла product_page.py
    product_page.should_not_be_success_message()      # выполнили метод should_not_be_success_message из файла product_page.py

def ttest_guest_cant_see_success_message(browser):
    product_page = ProductPage(browser, link)         # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    product_page.open()                               # выполняем метод "open" из base_page.py
    product_page.should_not_be_success_message()  # выполнили метод should_not_be_success_message из файла product_page.py

def ttest_message_disappeared_after_adding_product_to_basket(browser):
    product_page = ProductPage(browser, link)         # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    product_page.open()                               # выполняем метод "open" из base_page.py
    product_page.add_product_to_basket()              # выполнили метод add_product_to_basket из файла product_page.py
    product_page.should_success_message_disappear()   # выполнили метод should_success_message_disappear из файла product_page.py


def ttest_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def ttest_guest_can_go_to_login_page_from_product_page (browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_message_about_empty_basket()
    basket_page.should_be_no_item_block_in_basket()

