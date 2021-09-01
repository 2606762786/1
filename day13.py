#taobao

from selenium import webdriver
import time
driver = webdriver.firefox()
driver.get("http://www.taobao.com")
driver.maximize_window()
driver.find_element_by_class_name("").click()
time.sleep(10)
driver.find_element_by_id("").click()
driver.find_element_id("username").send_keys("")
driver.find_element_by_id("password").send_keys("")
driver.find_elemeynt_by_id("").click()



#jingdong
from selenium import webdriver
import time
driver = webdriver.firefox()
driver.get("http://www.jd.com/")
driver.maximize_window()
driver.find_element_by_partial_link_test("").click()
driver.find_element_by_partial_link_test("").click()
driver.find_element_by_id("username").send_keys("")
driver.find_element_by_id("password").send_keys("")
driver.find_element_by_id("").click()
time.sleep(10)
driver.find_element_by_id("").send_keys("")
driver.find_element_by_class_name_("").send_keys("")
driver.find_element_by_class_name_("").send_keys("")
