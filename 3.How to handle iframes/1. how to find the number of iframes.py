# # # Now i need to check how many iframes avilable in the page
# # # Doubt : Am not able perform this
# # # Where i have made mistakes



from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:/Users/LAL KRISHNA/PycharmProjects/12june2019/0.drivers/chromedriver.exe")
driver.get("https://phptravels.com/")

driver.maximize_window()
driver.implicitly_wait(20)
time.sleep(5)

# # # If we click on the allow button, then we get an alert.
# # Now we should perform the action inside the alert, for that we should move the control from our window to the alert
driver.find_element_by_xpath("//button[@id='onesignal-popover-allow-button']").click()
time.sleep(10)



