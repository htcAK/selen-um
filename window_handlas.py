from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
driver=webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://www.amazon.com")
amazon=driver.current_window_handle
print(amazon)
print(driver.title)
driver.switch_to.new_window() # içerisine widow yazarsak aynı sekmede farklı arama yapar
driver.get("https://www.hepsiburada.com")
hepsiburada=driver.current_window_handle
print(hepsiburada)
print(driver.title)
driver.switch_to.window(amazon)