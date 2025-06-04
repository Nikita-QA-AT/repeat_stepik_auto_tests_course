import math
from selenium.common.exceptions import NoAlertPresentException
from ..conftest import browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException
from .locators import BasePageLocators


class BasePage():
    def __init__(self, browser: WebDriver, url: str = None, timeout: int = 10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True



    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")



    def safe_click(self, locator, timeout=10, description="элемент"):
        try:
            WebDriverWait(self.browser, timeout).until(
                EC.element_to_be_clickable(locator)
            ).click()
            print(f"✅ Клик по элементу: {description}")
        except TimeoutException:
            raise AssertionError(
                f"❌ Не удалось кликнуть по элементу: {description}. Возможно, он неактивен или селектор неверный: {locator}")

    def safe_find(self, locator, timeout=10, description="элемент"):
        try:
            element = WebDriverWait(self.browser, timeout).until(
                EC.visibility_of_element_located(locator),
                message=f"❌ Не найден {description} за {timeout} секунд. Локатор: {locator}"
            )
            print(f"✅ Найден элемент: {description}")
            return element
        except TimeoutException as e:
            raise AssertionError(
                f"❌ Ошибка: {description} не найден за {timeout} секунд. Проверь локатор: {locator}"
            ) from e

    def safe_get_text(self, locator, timeout=10, description="элемент"):
        try:
            element = WebDriverWait(self.browser, timeout).until(
                EC.visibility_of_element_located(locator),
                message=f"❌ Не найден {description} за {timeout} секунд. Локатор: {locator}"
            )
            text = element.text  # важный момент — после явного ожидания
            print(f"✅ Получен текст '{text}' из: {description}")
            return text
        except StaleElementReferenceException:
            # попробуем повторно найти и взять текст (1 раз)
            try:
                element = WebDriverWait(self.browser, timeout).until(
                    EC.visibility_of_element_located(locator)
                )
                return element.text
            except Exception as e:
                raise AssertionError(f"❌ {description} стал недоступен из-за перерисовки. Локатор: {locator}") from e

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True

    def go_to_login_page(self):
        login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        login_link.click()


    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"


    def go_to_basket_page(self):
        login_link = self.browser.find_element(*BasePageLocators.GO_TO_BASKET_LINK)
        login_link.click()