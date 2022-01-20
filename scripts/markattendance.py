#!/usr/bin/env /Users/tradeindia/env/bin/python3

from selenium import webdriver
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options 
from getpass import getpass


usr=input("Enter User Name => ") 
pwd=getpass("Enter Password => ")
URL='http://housekeeping.tradeindia.com/'


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(URL)
print ("Opened Login Page")
sleep(1)
  
username_box = driver.find_element_by_name('username')
username_box.send_keys(usr)
print ("Username entered")
sleep(1)
  
password_box = driver.find_element_by_name('password')
password_box.send_keys(pwd)
print ("Password entered")

login_box = driver.find_element_by_name('Login')
login_box.submit()

driver.get('http://housekeeping.tradeindia.com/housekeeping/')
print ("Opened Housekeeping Page")
  
print ("Done")
