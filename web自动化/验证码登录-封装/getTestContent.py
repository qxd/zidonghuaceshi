from getDriver import SeleniumTool
# import time

#获取测试地址，及元素
class GetTestContent():
	def getNameAndPasswd(driver,name,passwd):
        #用户名
		driver.find_element_by_xpath("//*[@id='app']/div/div/div/div[3]/form/div[1]/div/div/input").send_keys(name)
        #密码
		driver.find_element_by_xpath("//*[@id='app']/div/div/div/div[3]/form/div[2]/div/div/input").send_keys(passwd)

	def getYzm(driver,yzm):
		#验证码
		driver.find_element_by_xpath("//*[@id='app']/div/div/div/div[3]/form/div[3]/div/div[1]/input").send_keys(yzm)
		#登录按钮
		driver.find_element_by_xpath("//*[@id='app']/div/div/div/div[3]/form/div[4]/div/button").click()
