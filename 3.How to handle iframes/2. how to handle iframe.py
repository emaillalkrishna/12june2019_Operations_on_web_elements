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
# # # First we have to loacte the iframe
phptravels_iframe =  driver.find_element_by_xpath("//div[@id='PopupSignupForm_0']/div[2]/div[2]/iframe")

# # # Then we have to switch the control from window to iframe
driver.switch_to.frame(phptravels_iframe)
driver.find_element_by_xpath("//input[@id='mc-EMAIL']").send_keys("lalkrishna@gmail.com")
driver.find_element_by_xpath("//div[@id='SignupForm_0']/div[2]/form/div[2]/input").click()
time.sleep(5)


# # # Now there are two cases
# # # Case 1 : If the email id is not exixting in the database, then easily we can move to the next step
# # # which is clicking the login button


# # # Case 2 : If the email id is existing in the database, then
# # # In this case as the email id is available in the database, application will thrown a warning message in the popup
# # # Now We need to close  this popup using the close button provided along with the popup box.
# # # But the close mark is kept outside the iframe
# # # But now our control is inside the iframe , to click on the close button we should come outside of iframe.
# # # Use the code showed below for that.
driver.switch_to.default_content()
driver.find_element_by_xpath('//*[@id="PopupSignupForm_0"]/div[2]/div[1]').click()
