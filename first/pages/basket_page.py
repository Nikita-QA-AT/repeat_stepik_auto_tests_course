from .base_page import BasePage
from .locators import BasketPageLocators
from ..conftest import browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasketPage(BasePage):

    def should_be_message_about_empty_basket(self):
        message_about_fullness_of_basket = self.safe_get_text(BasketPageLocators.MESSAGE_ABOUT_EMPTY_BASKET, description="Сообщение о наполненности корзины")
        assert "Ваша корзина пуста" in message_about_fullness_of_basket, f"expected text 'Ваша корзина пуста', but got {message_about_fullness_of_basket}"
        print(f"✅ Проверили, что сразу после перехода в корзину с главной страницы есть текст 'Ваша корзина пуста'")

    def should_be_no_item_block_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BLOCK_WITH_ITEMS_IN_BASKET), \
            "There are items in the basket, although they should not be"
        print(f"✅ Успешно проверили, что блок с товарами в корзине отсутствует")