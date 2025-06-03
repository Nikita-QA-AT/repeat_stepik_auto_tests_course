from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, ".login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    MESSAGE_ABOUT_SUCCESS_ADD_PRODUCT_TO_BASKET = (By.CSS_SELECTOR, ".alert-success .alertinner strong")
    TOTAL_SUM_IN_BASKET = (By.XPATH, "//div[contains(@class, 'alertinner')][contains(., 'Your basket total')]/p/strong")
    NAME_OF_PRODUCT = (By.CSS_SELECTOR, ".product_main h1")
    PRICE_OF_PRODUCT = (By.CSS_SELECTOR, ".product_main .price_color")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")




