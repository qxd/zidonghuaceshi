from chaojiying import Chaojiying
from PIL import Image

class Code():

	def getCode(driver):
		# 保存浏览器当前页面
		driver.save_screenshot("page.png")

		# 从页面中截取验证码
		vcode = driver.find_element_by_xpath("//*[@id='app']/div/div/div/div[3]/form/div[3]/div/div[2]/img")

		# 1、获取验证码上下左右边界左边
		loc = vcode.location
		print(loc)
		size = vcode.size
		print(size)
		left = loc['x'] * 2
		top = loc['y'] * 2
		right = (loc['x'] + size['width']) * 2
		button = (loc['y'] + size['height']) * 2

		# 截取页面中的验证码
		page_pic = Image.open('page.png')
		# 进行截图：参数时一个元组（left,top,right,button）
		v_code_pic = page_pic.crop((left, top, right, button))

		v_code_pic.save('yzm.png')

		# 利用超级鹰识别验证码中的内容，每次10分
		yz = Chaojiying(username='qxd123456', password='123456', soft_id='901845')

		with open('yzm.png', 'rb')as f:
			pic = f.read()

		# 得到验证码识别的结果
		result = yz.post_pic(pic, codetype='1004')['pic_str']
		return result

