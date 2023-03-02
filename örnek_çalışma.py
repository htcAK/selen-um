'''
1."https://www.python.org" sayfasina gidin.
2. Arama buttonuna tıklayın.
3. Kutucuğa "python" yazdırın.
4. GO butonuna tıklatın.
5. python butonuna tıklayıp anasayfaya dön.
6. sayfayı kapatın.

'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
import time

driver = driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()

driver .get ("https://www.python.org")
time .sleep(3)
driver.find_element(By.ID,"id-search-field").click()
time.sleep(3)
driver.find_element(By.ID,"id-search-field").send_keys("Python")
time .sleep(3)
driver. find_element(By.ID,"submit").click()
time.sleep(3)
time.sleep(3)
driver. quit()


from selenium import webdriver
from selenium .webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.apple.com.tr")

print(driver.title)
