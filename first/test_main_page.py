import pytest
import time
import math
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

link = "http://selenium1py.pythonanywhere.com/"

def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, link)                                 # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                                                    # выполняем метод "open" из base_page.py
    page.go_to_login_page()                                        # выполняем метод go_to_login_page()  из main_page.py
    login_page = LoginPage(browser, browser.current_url)           # инициализируем Page Object, передаем в конструктор экземпляр драйвера и текущий url
    login_page.should_be_login_page()                              # выполняем метод should_be_login_page  из login_page.py



def test_guest_should_see_login_link(browser):
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                      # открываем страницу
    page.should_be_login_link()      # выполняем метод страницы — проверяем наличие ссылки на страницу логина
