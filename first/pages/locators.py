from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, ".login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_EMAIL_INPUT = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_PASSWORD_INPUT = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_REPEAT_PASSWORD_INPUT = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, 'button[name="registration_submit"]')


class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    MESSAGE_ABOUT_SUCCESS_ADD_PRODUCT_TO_BASKET = (By.CSS_SELECTOR, ".alert-success .alertinner strong")
    TOTAL_SUM_IN_BASKET = (By.XPATH, "//div[contains(@class, 'alertinner')]//p/strong")
    NAME_OF_PRODUCT = (By.CSS_SELECTOR, ".product_main h1")
    PRICE_OF_PRODUCT = (By.CSS_SELECTOR, ".product_main .price_color")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    GO_TO_BASKET_LINK = (By.CSS_SELECTOR, ".btn-group .btn.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    MESSAGE_ABOUT_EMPTY_BASKET = (By.CSS_SELECTOR, "#content_inner")
    BLOCK_WITH_ITEMS_IN_BASKET = (By.CSS_SELECTOR, ".basket-items")




