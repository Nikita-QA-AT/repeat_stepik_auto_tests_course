import pytest
import time
import math
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"

def test_guest_can_add_product_to_basket(browser):
    product_page = ProductPage(browser, link)                      # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    product_page.open()                                            # выполняем метод "open" из base_page.py
    product_page.add_product_to_basket()                           # выполнили метод add_product_to_basket из файла product_page.py
    product_page.solve_quiz_and_get_code()                         # решаем пример и вводим ответ
    product_page.should_be_succes_message_about_add_product_to_basket_with_product_name()
    product_page.should_total_price_in_basket_equal_product_price()




