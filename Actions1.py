'''
        // once arama kutusuna click yapip
        // sonra harf harf Nutella yazisini yazdiralim
        // sonra da ENTER tusuna basalim
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time
driver=webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://www.amazon.com")
action=ActionChains(driver)
aramaKutusu=driver.find_element(By.ID,"twotabsearchtextbox")
action.click(aramaKutusu)\
.key_down(Keys.SHIFT)\
.send_keys("n")\
.key_up(Keys.SHIFT)\
.send_keys("u")\
.send_keys(Keys.ENTER)\
.perform()\
    
driver.quit()