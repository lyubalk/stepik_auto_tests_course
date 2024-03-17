from .base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import LoginPageLocators
from selenium.common.exceptions import NoSuchElementException


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Не верный URL, отсутствует login"
        # реализуйте проверку на корректный url адрес

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        try:
            self.browser.find_element(*LoginPageLocators.login_form)
        except NoSuchElementException:
            return False
        return True
        # log_form = self.browser.find_element()
        # assert WebDriverWait(self.browser, 10).until(EC.presence_of_all_elements_located((log_form))), "Формы логина на странице нет!"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        try:
            self.browser.find_element(*LoginPageLocators.register_form)
        except NoSuchElementException:
            return False
        return True
        # assert WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located(*LoginPageLocators.register_form)), "Формы логина на странице нет!"