from selenium.webdriver.common.by import By


class MainPageLocators:
    pass


class LoginPageLocators:
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")


class ProductPageLocators:
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.XPATH, "//*[contains(@class,'product_main')]/child::*[position()=1]")
    PRODUCT_PRICE = (By.XPATH, "//*[contains(@class,'product_main')]//*[contains(@class,'price_color')]")
    PRODUCT_NAME_SUCCESS_MESSAGE = (By.XPATH, "//*[contains(@class,'alert-success')][1]//strong")
    PRODUCT_PRICE_SUCCESS_MESSAGE = (By.XPATH, "//*[contains(@class,'alert-info')][1]//strong")
    SUCCESS_MESSAGE = (By.XPATH, "//*[contains(@class,'alert-success')]")


class BasePageLocators:
    LOGIN_LINK = (By.ID, "login_link")
    LOGIN_LINK_INVALID = (By.ID, "login_link_inc")
    BASKET_LINK = (By.XPATH, "//*[contains(@class,'basket-mini')]//a")
    BASKET_LINK_INVALID = (By.XPATH, "//*[contains(@class,'123basket-mini')]//a")


class BasketPageLocators:
    BASKET_ITEMS = (By.CSS_SELECTOR, "#content_inner #basket_formset")
    EMPTY_MESSAGE = (By.CSS_SELECTOR, "#content_inner > p")
