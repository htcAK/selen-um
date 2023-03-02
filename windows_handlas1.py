
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
driver=webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://www.amazon.com")
amazon=driver.current_window_handle
print(amazon)
print(driver.title)
driver.switch_to.new_window() # içerisine widow yazarsak aynı sekmede farklı arama yapar
driver.get("https://www.hepsiburada.com")
hepsiburada=driver.current_window_handle
print(hepsiburada)
print(driver.title)
driver.switch_to.new_window() # içerisine widow yazarsak aynı sekmede farklı arama yapar
driver.get("https://www.cimri.com")
cimri=driver.current_window_handle
print(cimri)
print(driver.title)
print(driver.window_handles)
def pencere_gecis(baslik):
    for sayfa in driver.window_handles:
        driver.switch_to.window(sayfa)
        if baslik in driver.title.lower():
           break
pencere_gecis("amazon")
print("amazon :",driver.title)
time.sleep(2)
pencere_gecis("hepsiburada")
print("hepsiburada :",driver.title)
driver.quit()