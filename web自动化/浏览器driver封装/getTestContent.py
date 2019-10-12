from getDriver import SeleniumTool
import time

#获取测试地址，及元素
class GetTestContent():

	def getUrlandElement(keys):
		driver = SeleniumTool.getDriver()
		driver.get('https://www.baidu.com')
		driver.find_element_by_id('kw').send_keys(keys)
		driver.find_element_by_id('su').click()
		#设置延时时间
		time.sleep(10)
		driver.close()
