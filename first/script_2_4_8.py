from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # Ждем пока цена (price) не снизится до 100$
    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

    # Нажимаем кнопку "Book"а
    browser.find_element(By.ID, "book").click()

    # считали x
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    value_x = x_element.text
    print(f"x = {value_x}")

    # посчитали answer
    answer = calc(int(value_x))
    print(f"answer = {answer}")

    # ввести ответ в текстовое поле
    answer_form = browser.find_element(By.CSS_SELECTOR, "#answer")
    answer_form.send_keys(str(answer))

    # Нажали кнопку "Submit"
    button_submit = browser.find_element(By.ID, "solve")
    button_submit.click()

    # Переключились на уведомление и скопировали ответ из него и вывели в терминал
    alert = browser.switch_to.alert
    print(f"ответ на задание = {alert.text.split()[-1]}")
    print(alert.text)
    alert.accept()


    # Вывели в консоль, что тест успешно пройден
    print(f"Тест успешно пройден")





finally:
    browser.quit()