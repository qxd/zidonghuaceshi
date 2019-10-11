#接口自动化框架: Httpclient\java net
#飞送后台————先登录，在拉取站点信息

import requests
#连接数据库
import pymysql
# 步骤

# 1.接口地址、链接
url = "https://feisongdev.ifeixiu.com/api/fs/v1/common/user/account"

# 2.请求参数
url += "?_allow_anonymous=true"

print(url)

# 3.请求方式get post

# 登录post
r = requests.post(
	url = url,
	data = {
		'identitykey': '18298020072',
		'password': '123456',
		'userType': 1,
		'terminalType': 3,
		'versionCode': 1,
		'appType': 1
	}
)
# print(r.json)
# 返回文本数据
# print(r.text)

# 返回字典格式的数据
# print(r.json()['data']['token'])

token = r.json()['data']['token']
# print(token)

# 4.调用工具进行发包——发数据包，发起一个请求 get
rw = requests.get(
	url = 'https://feisongdev.ifeixiu.com/api/fs/v1/backend/site-list',
    params = {
			'begin': 0,
			'count': 30,
			'status': 1,
			},
	headers = {'token': token}
	)

print(rw.text)


# 5.响应——把返回值提取出来

print(len(rw.json()['data']['list']))


# 6.断言——判断结果是否符合预期

#站点列表：https://feisongdev.ifeixiu.com/api/fs/v1/backend/site-list?begin=0&count=30&status=1



# 打开数据库连接﻿数据库	：3306		doBell123
db = pymysql.connect(host="47.98.191.13", user="root", password="doBell123", database='flysender_v1',charset='utf8')

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用 execute()  方法执行 SQL 查询
cursor.execute("SELECT * from fs_site order by createtime desc")

# 使用 fetchone() 方法获取单条数据. 使用 fetchall() 方法获取单条数据.
data = cursor.fetchall()

# 关闭数据库连接
db.close()
#第一条数据是否是最新建立id匹配

if rw.json()['data']['list'][0]['id'] == data[0][0]:
	print('返回数据正确')
else:
	print('返回数据错误')