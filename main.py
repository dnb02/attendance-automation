import time
from selenium import webdriver

# initializing driver
driver = webdriver.Chrome()

# going to the webpage
driver.get("https://lms.sssihl.edu.in/login/index.php")
time.sleep(5)

# finding the textboxes by element id
username = driver.find_element_by_id("username")
password = driver.find_element_by_id("password")


# using file io to import username and password
file = open("config.txt", 'r')
username_name, password_name = file.read().split(' ')
username.send_keys(username_name)
password.send_keys(password_name)


# finding and clicking the login button
loginbtn = driver.find_element_by_id("loginbtn")
time.sleep(5)
loginbtn.click()

# going to the attendance page
driver.get("https://lms.sssihl.edu.in/mod/attendance/view.php?id=1513")
time.sleep(5)

# Using Xpath
#xpath = //*[contains(@text,'Submit')]
# new_var = driver.find_element_by_xpath(//*[@href= 'https://lms.sssihl.edu.in/mod/attendance/'])
#xpath.click()
