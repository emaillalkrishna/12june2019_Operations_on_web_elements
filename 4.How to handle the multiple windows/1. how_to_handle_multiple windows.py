from selenium import webdriver
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

driver.find_element_by_xpath('//div[@id="PopupSignupForm_0"]//div[@class="mc-closeModal"]').click()
time.sleep(10)

# # # click on the login button

driver.find_element_by_xpath("//span[contains(text(),'Login')]").click()

# # # Another window will be opened in the same section, and we have to perform action in that second window

# # # But first find the id of the current window
current_window_id =  driver.current_window_handle
print(current_window_id)


# # # Find the iod of all opened windows
all_opened_window_ids = driver.window_handles
print(all_opened_window_ids)

# # # Now switch the control from the first window to the second window
driver.switch_to.window(all_opened_window_ids[1])
time.sleep(5)


# # # Now perform actions on second window
# # # Enter the user name
driver.find_element_by_xpath("//input[@id='inputEmail']").send_keys("admin")
time.sleep(5)

# Enter the password
driver.find_element_by_xpath("//input[@id='inputPassword']").send_keys("manager")


# # # Now go to the default content
# # driver.switch_to.default_content()
# # driver.find_element_by_xpath("//input[@id='inputPassword']")

# # Doubt :  How and why to find the active element
# # # The active element. What is that ?