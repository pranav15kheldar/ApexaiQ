"""Aaj Tak web Scrap"""
#Import Libries
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import pandas as pd

options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome()

driver.get("https://www.aajtak.in/")
time.sleep(3)

headline =driver.find_elements(By.XPATH , ".//h3")

list_of_headlines = []

for data in headline:
    list_of_headlines.append(data.text)
    print(list_of_headlines)


with open("/media/pranav-kheldar/New Volume/ApexaiQ_Program/CSV/aaj_tak.text", "w") as file:
    for item in list_of_headlines:
        file.write(item + "\n\n")