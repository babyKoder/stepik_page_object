from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.ID, "login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")


class ProductPageLocators:
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.XPATH, "//*[contains(@class,'product_main')]/child::*[position()=1]")
    PRODUCT_PRICE = (By.XPATH, "//*[contains(@class,'product_main')]//*[contains(@class,'price_color')]")
    PRODUCT_NAME_SUCCESS_MESSAGE = (By.XPATH, "//*[contains(@class,'alert-success')][1]//strong")
    PRODUCT_PRICE_SUCCESS_MESSAGE = (By.XPATH, "//*[contains(@class,'alert-info')][1]//strong")