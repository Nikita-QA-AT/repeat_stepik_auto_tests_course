import math
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from ..conftest import browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage():
    def __init__(self, browser, url, timeout=10):
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
                EC.presence_of_element_located(locator),
                message=f"❌ Не найден {description} за {timeout} секунд. Локатор: {locator}"
            )
            print(f"✅ Найден элемент: {description}")
            return element
        except TimeoutException as e:
            raise AssertionError(
                f"❌ Ошибка: {description} не найден за {timeout} секунд. Проверь локатор: {locator}"
            ) from e

