from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_basket_is_empty(self):
        assert self.is_element_present(*BasketPageLocators.MESSAGE_BASKET_IS_EMPTY), 'Basket is not empty'

    def should_no_products_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCTS_IN_BASKET), 'Products have in basket'