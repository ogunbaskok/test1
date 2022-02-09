from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


PATH = "C:\Program Files\chromedriver\chromedriver1.exe"

driver = webdriver.Chrome(PATH)
driver.maximize_window()
driver.get("https://google.com.tr")
time.sleep(3)
driver.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input").send_keys("trabzonspor")
driver.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input").send_keys(Keys.ENTER)

deger = driver.find_element_by_xpath("//*[@id='kp-wp-tab-overview']/div[1]/div/div/div/div/div/div[2]/div/div/div/span[2]").text
time.sleep(3)


a = 5
b = 7 

time.sleep(3)
print(deger)
print(deger)
print(deger)
print(deger)
print(deger)
print(deger)
print(deger)
print(deger)
print(deger)
print(deger)
print(deger)
print(deger)


time.sleep(5)
    
   