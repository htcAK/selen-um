from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
import time
driver=webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://demoqa.com/droppable")
actions =ActionChains(driver)
tutulan =driver.find_element(By.XPATH,'//*[@id="draggable"]')
bırakılan =driver.find_element(By.XPATH,'//*[@id="droppable"]')
actions.drag_and_drop(tutulan,bırakılan).perform()
time.sleep(15)
driver.quit()