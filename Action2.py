'''
     // facebook anasayfaya gidip
     // yeni kayit olustur butonuna basin
     // isim kutusunu locate edip,
     // geriye kalan alanlari TAB ile dolasarak
     // formu doldurun
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time
driver=webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://www.facebook.com")
a=driver.find_element(By.XPATH,"//a[@class='_42ft _4jy0 _6lti _4jy6 _4jy2 selected _51sy']")
a.click()
isimKutusu=driver.find_element(By.XPATH,"//input[@name='firstname']")
action=ActionChains(driver)
action.click(isimKutusu)\
.send_keys("mucteba")\
.send_keys(Keys.TAB)\
.send_keys("binici")\
.send_keys(Keys.TAB)\
.send_keys("78621486")\
.send_keys(Keys.TAB)\
.send_keys("şifre")\
.send_keys(Keys.TAB).perform()
time.sleep(3)
driver.quit()