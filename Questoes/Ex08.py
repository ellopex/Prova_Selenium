#https://www.selenium.dev/

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
import time


driver_path = "C:/Users/Jeane Peres/Documents/Gecko/geckodriver.exe"
service = Service(driver_path)
driver = webdriver.Firefox(service=service)

driver.get("https://www.selenium.dev/")

download = driver.find_element(By.XPATH, "//a[@class='nav-link' and @href='/downloads']")
download.click()
time.sleep(.5)
H1 = driver.find_element(By.XPATH, "//h1")
H2 = driver.find_element(By.XPATH, "//h2")


time.sleep(1)

print("H1: ", H1.text,"\nH2: ",H2.text)

driver.quit()

