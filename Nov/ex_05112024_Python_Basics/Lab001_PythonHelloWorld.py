import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service


edge_driver_path = "C:\Drivers\edgedriver_win64\msedgedriver.exe"
service = Service(edge_driver_path)
driver = webdriver.Edge(service=service)

driver.get("https://awesomeqa.com/webtable.html")
driver.maximize_window()



# Rows
#//table[contains(@id,"custo")]/tbody/tr
row_elements = driver.find_elements(By.XPATH,"//table[contains(@id,'custo')]/tbody/tr")
row = len(row_elements)
print(row)
# Cols
col_elements = driver.find_elements(By.XPATH,"//table[contains(@id,'custo')]/tbody/tr[2]/td")
col = len(col_elements)
print(col)
#//table[contains(@id,"custo")]/tbody/tr[2]/td

#First part- table[contains(@id,"custo")]/tbody/tr[
#7 - i (2,7)
#Second part- ]/td[
#3 - j (1,3)
#Third part- ]

first_part = "//table[contains(@id,'custo')]/tbody/tr["
second_part = "]/td["
third_part = "]"


for i in range(2,row+1):
    for j in range(1,col+1):
        dynamic_path = f"{first_part}{i}{second_part}{j}{third_part}"
        data = driver.find_element(By.XPATH, dynamic_path).text
        #print(data, end= " ")

        if "Helen Bennett" in data:
            country_path = f"{dynamic_path}/following-sibling::td"
            country_text = driver.find_element(By.XPATH, country_path).text
            print(f"Helen Bennett is in {country_text}")


