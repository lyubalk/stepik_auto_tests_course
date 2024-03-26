from .base_page import BasePage
from .locators import MainPageLocators, ProductPageLocators


class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.login_link)
        login_link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.login_link), "Login link is not presented"

    def go_to_basket(self):
        basket_link = self.browser.find_element(*ProductPageLocators.basket)
        basket_link.click()


