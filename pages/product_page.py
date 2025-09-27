from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        button.click()

    def should_be_product_added_to_basket(self):
        self.should_be_product_name_in_success_message()
        self.should_be_product_price_equal_to_product_price()

    def should_be_product_name_in_success_message(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        message_product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_SUCCESS_MESSAGE).text

        assert product_name == message_product_name, \
            (f'Product name in success message does not match. '
             f'Expected:{product_name}, got: {message_product_name}')

    def should_be_product_price_equal_to_product_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        message_product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_SUCCESS_MESSAGE).text

        assert product_price == message_product_price, \
            (f'Basket price does not match product price. '
             f'Expected {product_price}, got: {message_product_price}')
