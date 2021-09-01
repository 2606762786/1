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


#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import paramiko
import pyautogui
import os
from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from Auto_Test.base_action import match

def login_in():
    browser = webdriver.Firefox()
    browser.maximize_window()
    browser.get("https://mail.qq.com/")
    browser.switch_to.frame("login_frame")
    browser.find_element_by_class_name("inputstyle").clear()
    browser.find_element_by_class_name("inputstyle").send_keys("xxxxx")
    browser.find_element_by_class_name("inputstyle.password").clear()
    browser.find_element_by_class_name("inputstyle.password").send_keys("xxxxx")
    browser.find_element_by_id("login_button").click()
    browser.find_element_by_class_name("login_button").click()
    time.sleep(2)
    browser.switch_to.frame("tcaptcha_iframe")

    time.sleep(3)
    # 等待图片加载出来
    WebDriverWait(browser, 5, 0.5).until(
        EC.presence_of_element_located((By.ID, "tcaptcha_drag_button")))
    # button = browser.find_element_by_id('tcaptcha_drag_button')
    # x, y = button.location.get('x'), button.location.get('y')
    # print("location:",x,y)
    lx,ly=match("QQmail-slick")
    lz=[x for x in range(120,200,3)]
    for i in lz:
        pyautogui.moveTo(lx,ly)
        pyautogui.dragRel(i,0,duration=2,button='left')
        time.sleep(1)
        pyautogui.moveRel(-i,0)

        try:
            alert = browser.find_element_by_id('guideText').text
        except Exception as e:
            print('get alert error: %s' % e)
            alert = ''
        if alert:
            print(u'滑块位移需要调整: %s' % alert)
            sleep(3)
        else:
            print('滑块验证通过')
            browser.switch_to.parent_frame()  # 验证成功后跳回最外层页面
            break
