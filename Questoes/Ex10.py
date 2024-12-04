#https://the-internet.herokuapp.com/login

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
import time



driver_path = "C:/Users/Jeane Peres/Documents/Gecko/geckodriver.exe"
service = Service(driver_path)
driver = webdriver.Firefox(service=service)

driver.get("https://the-internet.herokuapp.com/login")

#elementos
username = driver.find_element(By.ID, "username")
senha = driver.find_element(By.ID, "password")
enviar = driver.find_element(By.XPATH, "//button[@class='radius' and @type='submit']")


time.sleep(1)
#auto
username.send_keys("tomsmith")
time.sleep(.3)
senha.send_keys("SuperSecretPassword!")
time.sleep(.2)
enviar.click()
time.sleep(1)

successMsg = driver.find_element(By.XPATH, "//div[contains(text(), 'You logged into a secure area!')]")
if successMsg.is_displayed():
    print("Sucesso!")
else:
    print("Algo deu errado.")


time.sleep(1)



driver.quit()

