from .main_page import MainPage
from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def test_guest_can_go_to_basket_page(self):
        page = MainPage(self.browser, self.url)
        page.open()
        page.go_to_basket()

    def test_product_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.confirmation).text
        book_name = self.browser.find_element(*ProductPageLocators.name_book).text
        assert product_name == book_name, "Название не совпадает!"

    def test_product_price(self):
        product_name = self.browser.find_element(*ProductPageLocators.price_basket).text[1:]
        book_name = self.browser.find_element(*ProductPageLocators.price_book).text[1:]
        assert product_name == book_name, "Цена не совпадает!"
