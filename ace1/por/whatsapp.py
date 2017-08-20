from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import os
 
# Replace below path with the absolute path
# to chromedriver in your computer

# chromedriver = "/home/arpit/Downloads/chromedriver"
# os.environ["webdriver.chrome.driver"] = chromedriver
print "0"
driver = webdriver.Chrome('/home/arpit/Downloads/chromedriver')
print "1"
driver.get("https://web.whatsapp.com/")
print "2"
wait = WebDriverWait(driver, 1)
print "3"
# Replace 'Friend's Name' with the name of your friend 
# or the name of a group 
target = '"Sagar Sharma Tc Nit"'
print "21"
 
# Replace the below string with your own message
string = "Bhai mail kr diya!!!"
print "25"
 
x_arg = '//span[contains(@title,' + target + ')]'
print x_arg
# group_title = wait.until(EC.presence_of_element_located((
    # By.XPATH, x_arg)))
# group_title.click()
inp_xpath = '//div[@class="input"][@dir="auto"][@data-tab="1"]'
input_box = wait.until(EC.presence_of_element_located((
    By.XPATH, inp_xpath)))
for i in range(100):
    input_box.send_keys(string + Keys.ENTER)
    time.sleep(1)