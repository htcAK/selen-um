
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time
driver=webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://www.amazon.com")
actions =ActionChains(driver)
account=driver.find_element(By.XPATH,'//*[@id="nav-link-accountList"]')
actions.move_to_element(account).perform()
time.sleep(7)
driver.quit()