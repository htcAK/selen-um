from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
import time
driver=webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/context_menu")
actions =ActionChains(driver)
sagClick=driver.find_element(By.ID,"hot-spot")
actions.context_click(sagClick).perform()
alertt=Alert(driver)
alertt.accept()
time.sleep(7)
driver.quit()






