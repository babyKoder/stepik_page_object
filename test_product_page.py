import pytest

from pages.product_page import ProductPage

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
def test_guest_can_add_product_to_basket(browser, query_param):
    # link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    # link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207" + query_param
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_to_basket()
    product_page.solve_quiz_and_get_code()

    product_page.should_be_product_added_to_basket()


@pytest.mark.xfail
def test_guest_cat_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_to_basket()
    product_page.solve_quiz_and_get_code()
    product_page.should_not_be_success_message_v1()


def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_not_be_success_message_v1()


def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_to_basket()
    product_page.solve_quiz_and_get_code()
    product_page.should_not_be_success_message_v2()