from selenium.webdriver import Keys
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
sürücü=webdriver.Chrome()
sürücü.maximize_window()
sürücü.get("https://www.trendyol.com")
time.sleep(3)
arama_kutusu=sürücü.find_element(By.XPATH, '//*[@id="sfx-discovery-search-suggestions"]/div/div/input')
time.sleep(3)
arama_kutusu.send_keys("bisiklet",Keys.ENTER)
time.sleep(3)
ara_asama=sürücü.find_element(By.XPATH,'//*[@id="container"]/div[3]/div[2]/div[2]/div')
time.sleep(2)
ara_asama.click()
time.sleep(2)
bisiklet_özellikleri=sürücü.find_element(By.XPATH,'//*[@id="search-app"]/div/div[1]/div[2]/div[4]/div[1]/div/div[4]/div[1]/a/div[1]/div[2]/div[2]')
bisiklet_özellikleri.click()
time.sleep(10)
sürücü.quit()