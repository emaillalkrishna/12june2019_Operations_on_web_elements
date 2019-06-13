# # # First we should install selenium package in our project
# # # then only we will be able to use the locators asociated to it
# # # Now we need to import the webdriver to this particular page from selenium

# from selenium import webdriver
#
# driver = webdriver.Chrome(executable_path="C:/Users/LAL KRISHNA/PycharmProjects/12june2019/1.drivers/chromedriver.exe")
# driver.get(url="https://www.google.com/")
# driver.maximize_window()
# driver.implicitly_wait(30)
#
# driver.find_element_by_tag_name()
# driver.find_element_by_id()
# driver.find_element_by_name()
# driver.find_element_by_class_name()
# driver.find_element_by_link_text()
# driver.find_element_by_partial_link_text()
# driver.find_element_by_xpath()
# driver.find_element_by_css_selector()



# # # # Relative xpath Writing

# # # 1.Tag - Attribute name - Attribute value Trio
# # # Type 1 : //tagename[@attribute name = "attribute value"]
# # # Case 1 : //tagename[@id = "attribute value"]
# # # Case 2 : //tagename[@name = "attribute value"]
# # # Case 3 : //tagename[@class_name = "attribute value"]

# # # 2.Chained xpath
# # # Case  : //tagename1[@attribute name1 = "attribute value1"] //tagename2[@attribute name2 = "attribute value2"]

# # # 3. and / or
# # # //tagename[@attribute name1 = "attribute value1" and @attribute name2 = "attribute value2"]
# # # //tagename[@attribute name1 = "attribute value1" or @attribute name2 = "attribute value2"]

# # # 4.Text
# # # //tagname[text()="text value"]

# # # 5.Contains
# # # Type 1 : //tagename[contains( @attribute name ,     "attribute value" ) ]
# # # Type 1 : //tagename[contains(      text()     ,        "text value"   )  ]