import requests

class TokenClass():
	def __init__(self):
		# self.headers = {
		# 	'Connection': 'keep-alive',
		# 	'Content-Type': 'application/json;charset=UTF-8',
		# }
		self.url = 'https://feisongdev.ifeixiu.com/api/fs/v1'

	def getToken(self):
		#post(url,data,headers)
		self.r = requests.post(
			self.url + "/common/user/account",
		    data = {
			    'identitykey': '18298020072',
			    'password': '123456',
			    'userType': 1,
			    'terminalType': 3,
			    'versionCode': 1,
			    'appType': 1
		        }
		)

		token = self.r.json()['data']['token']

		return token


	def getInfo(self, extraUrl):
		params = {
			'begin': 0,  #拉取0-30个
			'count': 30,
			'status': 1,  #状态为启用的
			'token': self.getToken()
		}

		headers = {'token': self.getToken()}  #token放在请求头中

		# get(url,params,headers)
		self.r = requests.get(self.url + extraUrl, params = params, headers = headers)
		return self.r
		# print(self.r.json())


