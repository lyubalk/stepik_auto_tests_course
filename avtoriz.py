from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://dev.prondo.co/account/login")
sleep(10)
username = driver.find_element(By.CSS_SELECTOR, 'input[autocomplete="email"]')
username.send_keys("lyubaosipova6@gmail.com")
driver.find_element(By.CSS_SELECTOR, 'button.MuiLoadingButton-root.MuiButton-root.MuiButton-contained.MuiButton-containedPrimary.MuiButton-sizeMedium.MuiButton-containedSizeMedium.MuiButton-fullWidth.MuiButtonBase-root.loginbox-fe-root-1bjm586').click()
# delete = driver.find_elements(By.CSS_SELECTOR, ".added-manually")
# print(len(delete))
sleep(15)