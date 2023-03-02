'''
        //● Bir metod olusturun: acceptAlert
        //○ 1. butona tıklayın, uyarıdaki OK butonuna tıklayın ve result mesajının
        //“You successfully clicked an alert” oldugunu test edin.
        https://the-internet.herokuapp.com/javascript_alerts
'''
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.alert import Alert
import time

driver=webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.find_element(By.XPATH,'//*[@id="content"]/div/ul/li[1]/button').click()
time.sleep(3)
alertt=Alert(driver)
alertt.accept()
basarı_mesajı=driver.find_element(By.XPATH,'//*[@id="result"]').text
time.sleep(3)
assert"You successfully clicked an alert"  in basarı_mesajı
driver.quit()