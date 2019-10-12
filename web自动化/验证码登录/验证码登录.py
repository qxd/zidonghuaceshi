

from selenium import webdriver
from chaojiying import Chaojiying
from PIL import Image

# 第一步： 创建一个浏览器
driver = webdriver.Chrome(executable_path='/Users/quxiaodan/Selenium-drivers/chromedriver')
# 访问登录页面
driver.get('http://dev.sixinfor.com:40030/login')

# 第二步：输入账号和密码

# 定位账号输入框
driver.find_element_by_xpath("//*[@id='app']/div/div/div/div[3]/form/div[1]/div/div/input").send_keys('1000500101080441')
driver.find_element_by_xpath("//*[@id='app']/div/div/div/div[3]/form/div[2]/div/div/input").send_keys('123456')
# 定位密码输入框

# 第三步：验证码识别

# 保存浏览器当前页面
driver.save_screenshot("page.png")

# 从页面中截取验证码
vcode = driver.find_element_by_xpath("//*[@id='app']/div/div/div/div[3]/form/div[3]/div/div[2]/img")

# 1、获取验证码上下左右边界左边
loc = vcode.location
print(loc)
size = vcode.size
print(size)
left = loc['x']*2
top = loc['y']*2
right = (loc['x'] + size['width'])*2
button = (loc['y'] + size['height'])*2

# 截取页面中的验证码
page_pic = Image.open('page.png')
# 进行截图：参数时一个元组（left,top,right,button）
v_code_pic = page_pic.crop((left,top,right,button))
v_code_pic.save('yzm.png')

# 识别验证码中的内容
yz = Chaojiying(username='qxd123456', password='123456', soft_id='901845')

with open('yzm.png','rb')as f:
    pic = f.read()


print(pic)
# 得到验证码识别的结果
result = yz.post_pic(pic,codetype='1004')
print('result===' )
print(result)
res = result['pic_str']
print('res==='+ res)
# 第四步：输入验证码
driver.find_element_by_xpath("//*[@id='app']/div/div/div/div[3]/form/div[3]/div/div[1]/input").send_keys(res)

# 第五步：点击登录
driver.find_element_by_xpath("//*[@id='app']/div/div/div/div[3]/form/div[4]/div/button").click()


