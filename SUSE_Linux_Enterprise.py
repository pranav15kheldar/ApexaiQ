"""SUSU Linux Enterprise Scrapping"""
#Import Libries
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd
import time

options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome()

#chrome instance
driver.get("https://en.wikipedia.org/wiki/SUSE_Linux_Enterprise")
time.sleep(1)

def table_1_scrap() :
    """Here we have scarp End of sechudle data table"""
    table_1 = driver.find_element(By.XPATH, ".//table[2]" )
    all_table_1_rows = table_1.find_elements(By.XPATH, ".//tr ")

    list_of_table_1_rows = []

    for each_row in all_table_1_rows:
        list_of_table_1_data = []
        all_table_1_data = each_row.find_elements(By.XPATH, " .//th | .//td")
        for data in all_table_1_data:
            list_of_table_1_data.append(data.text)
            print(list_of_table_1_data)
        list_of_table_1_rows.append(list_of_table_1_data)
    print(list_of_table_1_rows)

    #Created data Frame and CSV file 
    df = pd.DataFrame(list_of_table_1_rows[1:7], columns = list_of_table_1_rows[0])
    df.to_csv("/media/pranav-kheldar/New Volume/ApexaiQ_Program/CSV/SUSU Linx Enterpries Table1.csv", index = False)
    print(df)

def table_2_scrap():
    """Here we have scrap Release dates of SUSE Linux Enterprise Server versions Table"""
    table_2 = driver.find_element(By.XPATH, ".//table[3]")
    all_table_2_rows = table_2.find_elements(By.XPATH, ".//tr ")

    list_of_table_2_rows = []

    for each_row in all_table_2_rows:
        list_of_table_2_data = []
        all_table_2_data = each_row.find_elements(By.XPATH, " .//th | .//td")
        for data in all_table_2_data:
            list_of_table_2_data.append(data.text)
            print(list_of_table_2_data)
        list_of_table_2_rows.append(list_of_table_2_data)
    print(list_of_table_2_rows)

    #Created data Frame and CSV file 
    df = pd.DataFrame(list_of_table_2_rows[1:], columns = list_of_table_2_rows[0])
    df.to_csv("/media/pranav-kheldar/New Volume/ApexaiQ_Program/CSV/SUSU Linx Enterpries Table2.csv", index = False)
    print(df)


if __name__ == "__main__":
    table_1_scrap()
    table_2_scrap()
