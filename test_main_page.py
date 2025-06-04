import pytest
import time
import math

from first.pages.base_page import BasePage
from first.pages.main_page import MainPage
from first.pages.login_page import LoginPage
from first.pages.basket_page import BasketPage
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

link = "http://selenium1py.pythonanywhere.com/"

@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(self, browser):
        page = MainPage(browser, link)                                 # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()                                                    # выполняем метод "open" из base_page.py
        page.go_to_login_page()                                        # выполняем метод go_to_login_page()  из main_page.py
        login_page = LoginPage(browser, browser.current_url)           # инициализируем Page Object, передаем в конструктор экземпляр драйвера и текущий url
        login_page.should_be_login_page()                              # выполняем метод should_be_login_page  из login_page.py

    def test_guest_should_see_login_link(self, browser):
        page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()                      # открываем страницу
        page.should_be_login_link()      # выполняем метод страницы — проверяем наличие ссылки на страницу логина



def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_message_about_empty_basket()
    basket_page.should_be_no_item_block_in_basket()
