from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
import time


driver_path = "C:/Users/Jeane Peres/Documents/Gecko/geckodriver.exe"
service = Service(driver_path)
driver = webdriver.Firefox(service=service)
driver.get("https://www.google.com")

pesquisa = driver.find_element(By.NAME, "q")
pesquisa.send_keys("Python Selenium")
pesquisa.send_keys(Keys.RETURN)

time.sleep(2)

driver.save_screenshot("resultado.png")
driver.quit()
