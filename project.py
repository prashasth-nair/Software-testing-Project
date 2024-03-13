from selenium import webdriver
from selenium.webdriver.common.by import By 
import time
print("open website")
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.amazon.in")
time.sleep(3)
 
searchbar=driver.find_element(By.ID,'twotabsearchtextbox')
searchbar.send_keys("shoes")
searchbar.submit()

time.sleep(3)
lang=driver.find_element(By.ID,"icp-nav-flyout")
lang.click()
print("test")

time.sleep(3)
sub=driver.find_element(By.XPATH,'//*[@id="icp-save-button"]')
sub.click()
time.sleep(3)

sort=driver.find_element(By.ID,'a-autoid-0-announce')
sort.click()
driver.find_element(By.XPATH,'//*[@id="s-result-sort-select_1"]').click()
time.sleep(3)


# driver.execute_script("window.scrollTo(0,1080)")
# nextpage=driver.find_element(By.XPATH,'//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[69]/div/div/span/ul/li[2]/span/a')
# nextpage.click()
hamburger = driver.find_element(By.XPATH,'//*[@id="nav-hamburger-menu"]')
hamburger.click()

time.sleep(1)
best_seller = driver.find_element(By.XPATH,'//*[@id="hmenu-content"]/ul[1]/li[2]/a')
best_seller.click()
time.sleep(4)
hamburger = driver.find_element(By.XPATH,'//*[@id="nav-hamburger-menu"]')
hamburger.click()
time.sleep(1)
echo = driver.find_element(By.XPATH,'//*[@id="hmenu-content"]/ul[1]/li[8]/a')
echo.click()
time.sleep(10)
driver.close()
