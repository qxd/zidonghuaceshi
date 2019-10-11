from tokenClass import TokenClass

#拉取站点列表
case = TokenClass()
#拉取站点列表
case_1 = case.getInfo('/backend/site-list')
print(case_1.json())

if(case_1.json()['code'] == 0):
	print('恭喜，测试通过啦啦啦啦~~~~')

