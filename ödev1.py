from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver. maximize_window() 
driver.get("http://www.trendyol.com")

driver.find_element(By.CLASS_NAME,"category-header").click()
time.sleep(5)
driver.find_element(By.CLASS_NAME,"//*[@id='browsing-gw-homepage']/div/div/div/article[1]/div/div/div[2]/a[3]/img").click()
time.sleep(5)
driver.find_element(By.CLASS_NAME,"image-overlay-body").click()

driver.find_element(By.CLASS_NAME,"featured-information-header").click()

driver.quit()
