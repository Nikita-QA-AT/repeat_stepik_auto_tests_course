from .base_page import BasePage
from .locators import ProductPageLocators
from ..conftest import browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class ProductPage(BasePage):

    def add_product_to_basket(self):
        self.safe_click(ProductPageLocators.ADD_TO_BASKET_BUTTON, description="Кнопка 'Добавить в корзину'")

    def should_be_success_message_about_add_product_to_basket_with_product_name(self):
        product_name = self.safe_find(ProductPageLocators.NAME_OF_PRODUCT, description="название продукта").text
        success_message = self.safe_find(ProductPageLocators.MESSAGE_ABOUT_SUCCESS_ADD_PRODUCT_TO_BASKET, description="сообщение об успешном нахождении товара").text
        print(f"product name = {product_name}, success message = {success_message}")
        assert product_name in success_message, f"expected product name {product_name} in success message, but got {success_message} in success message"
        print(f"Проверили, что название книги есть в success message")


    def should_total_price_in_basket_equal_product_price(self):
        product_price = self.safe_find(ProductPageLocators.PRICE_OF_PRODUCT, description="цена продукта").text
        total_price_in_basket = self.safe_find(ProductPageLocators.TOTAL_SUM_IN_BASKET, description="итоговая цена в корзине").text
        print(f"total price = {total_price_in_basket}, product price = {product_price}")
        assert product_price in total_price_in_basket, f"expected product price {product_price} in total price, but got {total_price_in_basket} total price"
        print(f"Проверили, что после добавления одного товара в корзину цена в корзине становится равной цене товара")