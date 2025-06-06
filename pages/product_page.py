from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_add_to_basket_button(self):
        assert self.is_element_present(
            *ProductPageLocators.ADD_TO_BASKET_BUTTON), "Add to basket button is not present on Page"

    def add_to_basket(self):
        add_to_basket = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        if "promo" in self.browser.current_url:
            add_to_basket.click()
            self.solve_quiz_and_get_code()
        else:
            add_to_basket.click()

    def should_be_product_added_to_basket(self):
        self.should_be_product_name_in_message()
        self.should_be_basket_total_equal_to_product_price()

    def should_not_be_success_message(self):
        """Сообщение об успехе не должно появляться"""
        assert self.is_not_element_present(*ProductPageLocators.BASKET_SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_disappear_success_message(self):
        """Сообщение об успехе должно исчезнуть"""
        assert self.is_disappeared(*ProductPageLocators.BASKET_SUCCESS_MESSAGE), \
            "Success message did not disappear"

    def should_be_product_name_in_message(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        message = self.browser.find_element(*ProductPageLocators.BASKET_SUCCESS_MESSAGE).text
        assert product_name == message, f"Product name '{product_name}' not in message '{message}'"

    def should_be_basket_total_equal_to_product_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        basket_total = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL).text
        assert product_price == basket_total, f"Price '{product_price}' not equal to basket total '{basket_total}'"

