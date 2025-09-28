from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty(self):
        self.should_be_empty_message()
        self.should_not_be_products()
        self.should_be_correct_empty_message()

    def should_be_empty_message(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_MESSAGE), 'Basket is not empty'

    def should_not_be_products(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), 'Products have in basket'

    def should_be_correct_empty_message(self):
        empty_message = self.browser.find_element(*BasketPageLocators.EMPTY_MESSAGE).text
        assert 'Your basket is empty' in empty_message, f'Wrong empty message:{empty_message}'
