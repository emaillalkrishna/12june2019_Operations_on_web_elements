from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome(executable_path="C:/Users/LAL KRISHNA/PycharmProjects/08June2019/driver/chromedriver.exe")
driver.get("https://jqueryui.com/droppable/")
driver.maximize_window()
driver.implicitly_wait(30)
time.sleep(5)

jquery_iframe = driver.find_element_by_tag_name("iframe")
driver.switch_to.frame(jquery_iframe)
time.sleep(5)

ac_var = ActionChains(driver)
source_element = driver.find_element_by_id("draggable")
destinatoin_element = driver.find_element_by_id("droppable")
time.sleep(5)
ac_var.drag_and_drop(source_element, destinatoin_element).perform()
