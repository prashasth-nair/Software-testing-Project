from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep


driver = webdriver.Chrome()
driver.get("https://www.amazon.in/")
sleep(2)
hamburger = driver.find_element(By.XPATH,'//*[@id="nav-hamburger-menu"]')
hamburger.click()

sleep(1)
best_seller = driver.find_element(By.XPATH,'//*[@id="hmenu-content"]/ul[1]/li[2]/a')
best_seller.click()
sleep(4)
hamburger = driver.find_element(By.XPATH,'//*[@id="nav-hamburger-menu"]')
hamburger.click()
sleep(1)
echo = driver.find_element(By.XPATH,'//*[@id="hmenu-content"]/ul[1]/li[8]/a')
echo.click()
sleep(10)