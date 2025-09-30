import pytest
from faker import Faker

from pages.basket_page import BasketPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.product_page import ProductPage


@pytest.mark.basket
class TestBasketFromProductPage:
    query_params = ["/?promo=offer0",
                    "/?promo=offer1",
                    "/?promo=offer2",
                    "/?promo=offer3",
                    "/?promo=offer4",
                    "/?promo=offer5",
                    "/?promo=offer6",
                    pytest.param("/?promo=offer7", marks=pytest.mark.xfail),
                    "/?promo=offer8",
                    "/?promo=offer9"]

    @pytest.mark.parametrize('query_param', query_params)
    @pytest.mark.need_review
    def test_guest_can_add_product_to_basket(self, browser, query_param):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207" + query_param
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.add_to_basket()
        product_page.solve_quiz_and_get_code()

        product_page.should_be_product_added_to_basket()

    @pytest.mark.xfail
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.add_to_basket()
        product_page.solve_quiz_and_get_code()
        product_page.should_not_be_success_message_v1()

    def test_guest_can_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.should_not_be_success_message_v1()

    @pytest.mark.xfail
    def test_message_disappeared_after_adding_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.add_to_basket()
        product_page.solve_quiz_and_get_code()
        product_page.should_not_be_success_message_v2()

    @pytest.mark.need_review
    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser):
        link = "https://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        # page.add_to_basket() # проверка что тесты падают

        page.go_to_basket_page()
        basket_page = BasketPage(browser, browser.current_url)

        basket_page.should_be_empty()


@pytest.mark.login
class TestLoginFromProductPage:
    def test_guest_should_see_login_link_on_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_login_link()

    @pytest.mark.need_review
    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()

        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()


class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page_main = MainPage(browser, link)
        page_main.open()
        page_main.go_to_login_page()

        page_login = LoginPage(browser, browser.current_url)
        page_login.open()
        page_login.register_new_user(Faker().email(), Faker().password())

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
        product_page = ProductPage(browser, link)
        product_page.open()

        product_page.add_to_basket()
        product_page.solve_quiz_and_get_code()

        product_page.should_be_product_added_to_basket()

    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
        product_page = ProductPage(browser, link)
        product_page.open()

        product_page.should_not_be_success_message_v1()
