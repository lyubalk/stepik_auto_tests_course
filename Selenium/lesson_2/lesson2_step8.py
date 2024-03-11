from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

try:
    # Ваш код, который заполняет обязательные поля
    first_name = browser.find_element(By.CSS_SELECTOR, "[name='firstname']")
    first_name.send_keys("Ivan")
    last_name = browser.find_element(By.CSS_SELECTOR, "[name='lastname']")
    last_name.send_keys("Petrov")
    email = browser.find_element(By.CSS_SELECTOR, "[name='email']")
    email.send_keys("ivan_petrov@mail.ru")

    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла
    file = browser.find_element(By.CSS_SELECTOR, "#file")
    file.send_keys(file_path)

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(5)

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
