# 一、android虚拟机
	# 失败
# 二、android真机
	# 机型：M5 NOte  魅蓝 Note5
# 三、ios虚拟机
# 四、ios真机

import os
import time
import unittest

from selenium import webdriver
from lib2to3.pgen2.driver import Driver
from lib2to3.tests.support import driver
from appium import webdriver
from selenium.webdriver.common.keys import Keys

PATH=lambda p:os.path.abspath(os.path.join(os.path.dirname(__file__),p))

# 指定需要的能力 capability
caps = {}
caps["automationName"] = "Appium"
caps["platformName"] = "android"
caps["platformVersion"] = "7.0"
caps["deviceName"] = "621QECQ93YHWU"   #设备名称 或 模拟器（如：127.0.0.1：62001）
# caps["deviceName"] = "360手机 N4S"
caps['appPackage'] = 'com.ifeixiu.flysender.debug'  #指定app
caps['appActivity'] = 'com.jxf.splashmodule.ui.SplashActivity'  #指定页面



#如果设置的是app在电脑上的路径，则不需要配appPackage和appActivity，同理反之

# appium 服务
driver = webdriver.Remote("http://0.0.0.0:4723/wd/hub", caps)

#获取元素并操作
# 地理位置权限
quanxian_1 = driver.find_element_by_id('com.android.packageinstaller:id/permission_allow_button')
# print(switch)
quanxian_1.click()
#手机存储权限
quanxian_2 = driver.find_element_by_id('com.android.packageinstaller:id/permission_allow_button')
# print(switch)
quanxian_2.click()

#拨打电话权限
quanxian_3 = driver.find_element_by_id('com.android.packageinstaller:id/permission_allow_button')
# print(switch)
quanxian_3.click()

#手机识别码权限
quanxian_4 = driver.find_element_by_id('com.android.packageinstaller:id/permission_allow_button')
quanxian_4.click()

# 进入用户名密码登录
# packege:com.ifeixiu.flysender.debug
# class: android.widget.TextView
# resource-id: com.ifeixiu.flysender.debug:id/tv_switch_login

switch_login = driver.find_element_by_id('com.ifeixiu.flysender.debug:id/tv_switch_login')
switch_login.click()

#用户名和密码 同一个id或class，使用find_elements_by_XXX

userName = driver.find_elements_by_id('com.ifeixiu.flysender.debug:id/edit_text')[0]
print(userName)
userName.send_keys('18298020072')

password = driver.find_elements_by_id('com.ifeixiu.flysender.debug:id/edit_text')[1]
print(password)
password.send_keys('123456')

#收起键盘
driver.hide_keyboard()

login = driver.find_element_by_id('com.ifeixiu.flysender.debug:id/btn_comfirm')
login.click()


# driver.quit()