from selenium import webdriver
#获得一个做自动化的驱动对象

class SeleniumTool:

	def getDriver():
		#读取config.propertoes文件中的
		with open("/Users/quxiaodan/Documents/python_work/自动化测试学习/web自动化/浏览器driver封装/config.properties") as file_object:
			browserType = file_object.read()
			print(browserType)

		if browserType == 'firefox':
			driver = webdriver.Firefox(executable_path='/Users/quxiaodan/Selenium-drivers/geckodriver')
			return driver

		if browserType == 'chrome':
			driver = webdriver.Chrome(executable_path='/Users/quxiaodan/Selenium-drivers/chromedriver')
			return driver
