from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time


driver = webdriver.Chrome(executable_path="C:/Users/LAL KRISHNA/PycharmProjects/12june2019/1.drivers/chromedriver.exe")
driver.get("https://phptravels.com/")

driver.maximize_window()
driver.implicitly_wait(20)
time.sleep(5)

# # # If we click on the allow button, then we get an alert.
# # Now we should perform the action inside the alert, for that we should move the control from our window to the alert
driver.find_element_by_xpath("//button[@id='onesignal-popover-allow-button']").click()
time.sleep(10)

phptravels_iframe =  driver.find_element_by_xpath("//div[@id='PopupSignupForm_0']/div[2]/div[2]/iframe")
driver.switch_to.frame(phptravels_iframe)
driver.find_element_by_xpath("//input[@id='mc-EMAIL']").send_keys("lalkrishna@gmail.com")
driver.find_element_by_xpath("//div[@id='SignupForm_0']/div[2]/form/div[2]/input").click()
time.sleep(5)
driver.find_element_by_xpath('//*[@id="PopupSignupForm_0"]/div[2]/div[1]').click()
