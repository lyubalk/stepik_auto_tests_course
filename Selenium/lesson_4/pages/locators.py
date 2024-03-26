from selenium.webdriver.common.by import By


class MainPageLocators():
    login_link = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    login_form = (By.ID, "login_form")
    register_form = (By.ID, "register_form")


class ProductPageLocators():
    basket = (By.CLASS_NAME, "btn.btn-lg.btn-primary")
    confirmation = (By.CSS_SELECTOR, 'div.alertinner > strong')
    name_book = (By.CSS_SELECTOR, 'div.row h1')
    confirmation_price = (By.XPATH, '//p[contains(text(), "Стоимость корзины теперь составляет")]')
    price_basket = (By.CSS_SELECTOR, 'div.alertinner > p > strong ')
    price_book = (By.CSS_SELECTOR, 'h1 + .price_color')

    pass
