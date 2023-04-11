# from selenium import webdriver
# from selenium.webdriver.edge import service
# from selenium.webdriver.remote import webelement
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support import expected_conditions as EC
# import time
# import os
# from datetime import datetime
# from selenium.webdriver import ActionChains

# with open("temp.csv", 'r') as csvfile:
#     rows=[row.strip('\n') for row in csvfile]
# # print(rows)
# option = webdriver.EdgeOptions()
# # option.use_chromium = True
# # # driver = webdriver.Edge(options=option)
# # option.add_argument('--ignore-certificate-errors')
# # option.add_argument("--test-type")

# driver = webdriver.Edge(executable_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe", options = option)
# driver.get("www.bing.com/")
# inputElement = driver.find_element_by_id("sb_form_ic")
# inputElement.send_keys(rows[3])
# # inputElement.send_keys(Keys.ENTER)


from selenium.webdriver.edge.options import EdgeOptions

from selenium import webdriver

# create a new instance of Edge
option = EdgeOptions()
browser = webdriver.Edge()



browser = webdriver.Edge(options=option)

# navigate to a webpage
browser.get("https://www.bing.com")
