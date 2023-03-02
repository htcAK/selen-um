'''
     // facebook anasayfaya gidip
     // yeni kayit olustur butonuna basin
     // isim kutusunu locate edip,
     // geriye kalan alanlari TAB ile dolasarak
     // formu doldurun
     // faker kullanarak yapalım
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from faker import Faker
import time
driver=webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://www.facebook.com")
a=driver.find_element(By.XPATH,"//a[@class='_42ft _4jy0 _6lti _4jy6 _4jy2 selected _51sy']")
a.click()
isimKutusu=driver.find_element(By.XPATH,"//input[@name='firstname']")
action=ActionChains(driver)
fakerr=Faker()
action.click(isimKutusu)\
.send_keys(fakerr.first_name())\
.send_keys(Keys.TAB)\
.send_keys(fakerr.last_name())\
.send_keys(Keys.TAB)\
.send_keys(fakerr.email())\
.send_keys(Keys.TAB)\
.send_keys(fakerr.password())\
.send_keys(Keys.TAB)\
.send_keys(fakerr.password()).perform()
time.sleep(3)
driver.quit()