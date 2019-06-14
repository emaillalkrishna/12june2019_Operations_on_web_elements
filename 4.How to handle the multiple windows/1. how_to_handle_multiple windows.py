from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time


driver = webdriver.Chrome(executable_path="C:/Users/LAL KRISHNA/PycharmProjects/12june2019/0.drivers/chromedriver.exe")
driver.get("https://phptravels.com/")

driver.maximize_window()
driver.implicitly_wait(20)
time.sleep(5)

# # # If we click on the allow button, then we get an alert.
# # Now we should perform the action inside the alert, for that we should move the control from our window to the alert
driver.find_element_by_xpath("//button[@id='onesignal-popover-allow-button']").click()
time.sleep(10)

# phptravels_iframe1 =  driver.find_element_by_xpath("//div[@id='PopupSignupForm_0']/div[2]/div[2]/iframe")
# driver.switch_to.frame(phptravels_iframe1)
# driver.find_element_by_xpath("//input[@id='mc-EMAIL']").send_keys("lalkrishna@gmail.com")
# driver.find_element_by_xpath("//div[@id='SignupForm_0']/div[2]/form/div[2]/input").click()
# time.sleep(5)

# # # Now as we have provided the emai-ld, iframe pop up is closed automatically and we have reached the main web page
# # # But Now again try to run the same code
# # # In this case as the email id is available in the database, application will thrown a warning message.

# driver.find_element_by_xpath('//*[@id="PopupSignupForm_0"]/div[2]/div[1]').click() # # Doubt : NoSuchElementException
driver.find_element_by_xpath('//div[@id="PopupSignupForm_0"]//div[@class="mc-closeModal"]').click()
time.sleep(10)

# # # click on the login button
# # # Another window will open in the same section, and we have to perform action in that second window

driver.find_element_by_xpath("//span[contains(text(),'Login')]").click()

current_window_id =  driver.current_window_handle
print(current_window_id)

all_opened_window_ids = driver.window_handles
print(all_opened_window_ids)

# # # Now take the control from the first window to the second window
driver.switch_to.window(all_opened_window_ids[1])


# # # Now perform actions on second window
driver.find_element_by_xpath("//input[@id='inputEmail']").send_keys("lalkrishna@gmail.com")
# driver.find_element_by_xpath("//input[@id='inputPassword']")

#
# # # # Now find the active element and default content
# driver.switch_to.default_content()
# driver.find_element_by_xpath("//input[@id='inputPassword']")

