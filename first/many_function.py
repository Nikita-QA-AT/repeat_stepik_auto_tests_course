import pytest
import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException






@pytest.mark.parametrize('lesson_id', ["236895",
                                       "236896",
                                       "236897",
                                       "236898",
                                       "236899",
                                       "236903",
                                       "236904",
                                       "236905"
                                       ])
def test_stepik_authorization_and_answer_submission(browser, lesson_id):
    link = f"https://stepik.org/lesson/{lesson_id}/step/1"
    browser.get(link)

    # Т.к. страница долго грузится, то ждем пока искомый элемент (кнопка "Войти") станет кликабельным и после этого → нажимаем на кнопку "Войти"
    login_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#ember480"))
    )
    login_button.click()

    # Ввели значение в поле e-mail
    email_input = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#id_login_email"))
    )
    email_input.send_keys("olkin-nikita@mail.ru")

    # Ввели значение в поле пароль
    password_input = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#id_login_password"))
    )
    password_input.send_keys("326072")

    # Нажали на кнопку "Войти"
    login_submit_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".sign-form__btn.button_with-loader"))
    )
    login_submit_button.click()

    print(f"Авторизовались")



    # Проверка на наличие кнопок "Решить снова" или "Начать сначала (сброс)
    try:
        # Ждём до 10 секунд появления хотя бы одной кнопки "Решить снова" или "Начать сначала (сброс)"
        again_button = WebDriverWait(browser, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".again-btn.white"))
        )
        print(f"была кнопка Решить снова и мы ее нажали")
        again_button[0].click()

        try:
            ok_button = WebDriverWait(browser, 3).until(
                EC.element_to_be_clickable((By.XPATH, "//button[text()='OK']"))
            )
            print("Окно подтверждения появилось — нажимаем ОК")

            # Запоминаем старый input перед нажатием OK
            old_input = WebDriverWait(browser, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".ember-text-area"))
            )
            ok_button.click()

            # Ждём, пока старый input исчезнет (DOM обновится)
            WebDriverWait(browser, 10).until(
                EC.staleness_of(old_input)
            )

            # Ждём, пока появится новый input
            WebDriverWait(browser, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".ember-text-area"))
            )
        except TimeoutException:
            print("Окно подтверждения не появилось — продолжаем")

    except TimeoutException:
        print(f"Кнопок Решить снова или Начать сначала (сброс) не было")

    # Решаем задачу
    answer = str(math.log(int(time.time())))
    print(f"посчитали answer")

    # Ждём появления поля для ввода ответа и вводим туда результат
    answer_input = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".ember-text-area"))
    )
    answer_input.clear()  # <--- очищаем поле перед вводом
    answer_input.send_keys(answer)
    print(f"ввели answer в поле ввода")


    # Нажимаем кнопку "Отправить"
    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".submit-submission"))
    ).click()
    print(f"Нажали кнопку Отправить")

    # Дожидаемся фидбека о том, что ответ правильный
    feedback = WebDriverWait(browser, 12).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".smart-hints__hint"))
    )
    feedback_text = feedback.text
    print(f"Получили фидбек: {feedback_text}")

    # Проверяем, что фидбек равен "Correct!"
    assert feedback_text == "Correct!", f"Ожидали 'Correct!', но получили '{feedback_text}'"
    print("Фидбек корректный — 'Correct!'")

    print(f"Тест успешно пройден")

