from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/iframe")
frame=driver.find_element(By.ID,"mce_0_ifr")
driver.switch_to.frame(frame)
time.sleep(2)
driver.find_element(By.ID,("tinymce")).clear()
driver.find_element(By.ID,("tinymce")).send_keys("frame burasi ")
driver.switch_to.default_content()
elemet=driver.find_element(By.CSS_SELECTOR,"#page-footer > div > div > a")
assert  elemet.is_displayed()
print(elemet.text)
driver.quit()