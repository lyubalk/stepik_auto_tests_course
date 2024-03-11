from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)


    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))


    element = browser.find_element(By.ID, "treasure")
    x_element = element.get_attribute("valuex")
    y = calc(x_element)

    inpyt_1 = browser.find_element(By.ID, "answer")
    inpyt_1.send_keys(y)

    robot = browser.find_element(By.ID, "robotCheckbox").click()
    # time.sleep(3)

    first_name = browser.find_element(By.ID, "robotsRule").click()

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-default")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(5)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
