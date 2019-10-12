#安徽思政系统登录 20191012

from selenium import webdriver
from getDriver import SeleniumTool
from getTestContent import GetTestContent
from getCode import Code

# 指定driver
driver = SeleniumTool.getDriver()
driver.get('http://dev.sixinfor.com:40030/login')

# 输入用户名和密码
GetTestContent.getNameAndPasswd(driver,'1000500101080441', '123456')

# 获得验证码
result = Code.getCode(driver)

# 输入验证码点击登录

GetTestContent.getYzm(driver,result)




