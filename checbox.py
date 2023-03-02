'''
        //a. Verilen web sayfasına gidin.
        //https://the-internet.herokuapp.com/checkboxes
        //b. Checkbox1 ve checkbox2 elementlerini locate edin.
        //c. Checkbox1 seçili değilse onay kutusunu tıklayın
        //d. Checkbox2 seçili değilse onay kutusunu tıklayın
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver =webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://the-internet.herokuapp.com/checkboxes")
chex_1=driver.find_element(By.XPATH,"(//input[@type='checkbox'])[1]")
chex_2=driver.find_element(By.XPATH,"(//input[@type='checkbox'])[2]")
time.sleep(5)
if not chex_1.is_selected():
    chex_1.click()
if not chex_2.is_selected():
    chex_2.click()
driver.quit()