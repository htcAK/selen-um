from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#implicity wait
#explicity wait
driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://www.geeksforgeeks.org/")
element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable  ((By.link_text, "Courses"))
        )
# click the element
element.click()