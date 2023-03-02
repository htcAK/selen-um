from selenium import webdriver
from selenium .webdriver.common.by import By
import time

driver=webdriver . Chrome()
driver .implicitly_wait(5)
driver.maximize_window()

driver.get("https://www.trendyol.com")
driver.find_element(By.XPATH,'//*[@id="Combined-Shape"]').click()
trend_url=driver.current_url
print(trend_url)

assert "trendyol" in trend_url
title=driver.title
print(title)

assert not "hepsiburada" in title
trend_logo=driver.find_element(By.ID,"logo")
#assert trend_logo .is_displayed()
if trend_logo.is_displayed():
   print("logo var")
driver.quit()