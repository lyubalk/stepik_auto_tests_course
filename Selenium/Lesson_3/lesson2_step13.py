from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest


class Test_unittest(unittest.TestCase):
    def test_step1(self):
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/registration1.html")
        first_name = browser.find_element(By.CLASS_NAME, "first_block .first")
        first_name.send_keys("Ivan")
        email = browser.find_element(By.CLASS_NAME, "first_block .third")
        email.send_keys("ivan_petrov@mail.ru")
        last_name = browser.find_element(By.CLASS_NAME, "first_block .second")
        last_name.send_keys("Petrov")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы

        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Тест  не пройден!")

    def test_step2(self):
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/registration2.html")
        first_name = browser.find_element(By.CLASS_NAME, "first_block .first")
        first_name.send_keys("Ivan")
        email = browser.find_element(By.CLASS_NAME, "first_block .third")
        email.send_keys("ivan_petrov@mail.ru")
        last_name = browser.find_element(By.CLASS_NAME, "first_block .second")
        last_name.send_keys("Petrov")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы

        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Тест  не пройден!")


""" if __name__ == "__main__":
    unittest.main()"""