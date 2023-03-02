'''
       amazon'a gidip
       dropdown'dan books secenegini secip
       Java aratalim
       ve arama sonuclarinin Java icerdigini test edelim
'''
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
driver=webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https:/www.amazon.com")
drop_down =driver.find_element(By.XPATH,'//*[@id="searchDropdownBox"]')
select=Select(drop_down)
amazon_kategoriler=select.options
for ktgr in amazon_kategoriler:
    print(ktgr.text)
books=select.select_by_visible_text("Books")
driver.find_element(By.ID,"twotabsearchtextbox").send_keys("paython",Keys.ENTER)
time.sleep(3)
