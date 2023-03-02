'''
 http://zero.webappsecurity.com sayfasina gidin
2. Signin buttonuna tiklayin
3. Login alanine  "username" yazdirin
4. Password alanine "password" yazdirin
5. Sign in buttonuna tiklayin (hata mesaji icin back tusuna tiklayin)
6. Online Banking menusunden Pay Bills sayfasina gidin
7. amount kismina yatirmak istediginiz herhangi bir miktari yazin
8. tarih kismina "2020-09-10" yazdirin
9. Pay buttonuna tiklayin
10. "The payment was successfully submitted." mesajinin ciktigini kontrol edin

'''

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
driver.get(" http://zero.webappsecurity.com")
driver.find_element(By.ID,"signin_button").click()
driver.find_element(By.NAME,"user_login").send_keys("username")
driver.find_element(By.NAME,"user_password").send_keys("password")
driver.find_element(By.NAME,"submit").click()
driver.back()
driver.find_element(By.XPATH,'//*[@id="onlineBankingMenu"]/div/strong').click()
driver.find_element(By.ID,"pay_bills_link").click()
driver.find_element(By.CLASS_NAME,"span1").send_keys("10000")
driver.find_element(By.ID,"sp_date").send_keys("2020-09-10")
driver.find_element(By.ID,"pay_saved_payees").click()
sonucYazisiElementi= driver.find_element(By.ID,("alert_content"))
print(sonucYazisiElementi.text)
if sonucYazisiElementi.is_displayed():
     print("test PASSED")
else:
    print("test FAILED")
time.sleep(3)
driver.quit()