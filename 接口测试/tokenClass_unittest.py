import requests
import unittest

class TokenClass(unittest.TestCase):
	def setUp(self):
		self.headers = {
			'Connection': 'keep-alive',
			'Content-Type': 'application/json;charset=UTF-8',
		}
		self.url = 'https://feisongdev.ifeixiu.com/api/fs/v1'

	def getToken(self):

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


	def test_getInfo(self):
		# self.getToken()
		params = {
			'begin': 0,
			'count': 30,
			'status': 1,
			'token': self.getToken()
		}

		headers = {'token': self.getToken()}

		self.r = requests.get(self.url + '/backend/site-list', params = params, headers = headers)


if __name__ =='__main__':
	suite = unittest.TestLoader().loadTestsFromTestCase(TokenClass)
	unittest.TextTestRunner(verbosity = 2).run(suite)