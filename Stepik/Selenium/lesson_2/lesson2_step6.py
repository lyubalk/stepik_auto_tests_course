from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    link = "https://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)


    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))


    element = browser.find_element(By.ID, "input_value")
    x_element = element.text
    y = calc(x_element)

    inpyt_1 = browser.find_element(By.ID, "answer")
    inpyt_1.send_keys(y)

    robot = browser.find_element(By.ID, "robotCheckbox")
    browser.execute_script("return arguments[0].scrollIntoView(true);", robot)
    robot.click()

    # robot = browser.find_element(By.ID, "robotCheckbox").click()
    # time.sleep(3)

    first_name = browser.find_element(By.ID, "robotsRule").click()

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(5)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
