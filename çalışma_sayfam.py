
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
driver=webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()

driver .get ("https://tr.wikipedia.org/wiki/Anasayfa")
seçkin_madde_alanı=driver.find_element(By.ID,"mp-tfa")
metin_yazısı=seçkin_madde_alanı.text
print(metin_yazısı)

metin_yazısı=metin_yazısı.split(",")[0]
print(metin_yazısı)

kaliteli_madde= driver.find_element(By.ID,"mf-tfp").text
kaliteli_madde=kaliteli_madde.split(",")[0]
print(kaliteli_madde)

time.sleep(3)
driver.quit()