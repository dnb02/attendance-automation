from selenium import webdriver
driver = webdriver.Chrome()
# using xpath to find the submit attendance butt

attend =  //*[contains(@href,'lms.sssihl.edu.in/mod/attendance')]

# or
new_var = driver.find_element_by_xpath(//*[contains(text(), 'Submit Attendance')])
