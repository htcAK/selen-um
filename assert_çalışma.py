'''
    amazon ana sayfaya gidin
    üc farkli test method'u olusturarak asagidaki gorevleri yapin
    1- Url'in amazon icerdigini test edin
    2- title'in facebook icermedigini test edin
    3- sol ust kosede amazon logosunun gorundugunu test edin
'''
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://www.amazon.com")
amazon_url=driver.current_url
print(amazon_url)
assert "amazon" in amazon_url
tittle=driver.title
print(tittle)
assert not "facobook" in tittle
logo=driver.find_element(By.XPATH,'//*[@id="nav-logo-sprites"]')
#assert logo.is_displayed
if logo.is_displayed:
    print("evet logo var")
driver.quit()