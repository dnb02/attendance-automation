import time
from selenium import webdriver

# initializing driver
driver = webdriver.Chrome()

# going to the webpage
driver.get("https://lms.sssihl.edu.in/login/index.php")
time.sleep(1)

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
time.sleep(1)
loginbtn.click()

# going to the attendance page
try:
    xpath = driver.find_element_by_xpath("//button[@class='btn nav-link float-sm-left mr-1 btn-secondary']")
    xpath.click()
xpath = driver.find_element_by_xpath("//a[@data-key='400']")
xpath.click()
xpath = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/div/section[1]/div/div/ul/li[1]/div[3]/ul/li[5]/div/div/div[2]/div/a")
xpath.click()
