""" from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)
button = browser.find_element(By.TAG_NAME, "button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click() """

""" s = 'My Name is Julia'

if 'Name' in s:
    print('Substring found')

index = s.find('Name')
if index != -1:
    print(f'Substring found at index {index}') """

"""import unittest


class TestAbs(unittest.TestCase):
    def test_abs1(self):
        self.assertEqual(abs(-42), -42, "Should be absolute value of a number")

    def test_abs2(self):
        self.assertEqual(abs(-42), 42, "Should be absolute value of a number")


if __name__ == "__main__":
    unittest.main()"""
from selenium import webdriver

driver = webdriver.Firefox()
driver.get("https://stepik.org/lesson/25969/step/8")
