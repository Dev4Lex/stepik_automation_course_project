from multiprocessing.resource_tracker import register

from .base_page import BasePage
from .locators import MainPageLocators
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.browser.current_url == "https://selenium1py.pythonanywhere.com/en-gb/accounts/login/", f"Login URL is not {self.browser.current_url}"

    def should_be_login_form(self):
        login_form = self.browser.find_element(*LoginPageLocators.LOGIN_FORM)
        assert login_form, "Login form is not present on Page"

    def should_be_register_form(self):
        register_form = self.browser.find_element(*LoginPageLocators.REGISTRATION_FORM)
        assert register_form, "Register form is not present on Page"