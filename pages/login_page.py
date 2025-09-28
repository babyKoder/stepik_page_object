from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # print(self.browser.current_url)
        assert 'accounts' in self.browser.current_url, 'Url not contain a login'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Registration form is not presented"

    def register_new_user(self, email, password):
        print(f'email:{email}, pass:{password}')
        input_email = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL_ADDRESS)
        input_pass = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD)
        input_confirm_pass = self.browser.find_element(*LoginPageLocators.REGISTER_CONFIRM_PASSWORD)
        btn_register = self.browser.find_element(*LoginPageLocators.BUTTON_REGISTER)

        input_email.send_keys(email)
        input_pass.send_keys(password)
        input_confirm_pass.send_keys(password)
        btn_register.click()

        self.should_be_authorized_user()
