#连接数据库
import pymysql

# 打开数据库连接﻿数据库	：3306		doBell123
# db = pymysql.connect(host="localhost", user="root", password="123456", database='FlyRepair_v3',charset='utf8')
db = pymysql.connect(host="47.98.191.13", user="root", password="doBell123", database='flysender_v1',charset='utf8')

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用 execute()  方法执行 SQL 查询
cursor.execute("SELECT * from fs_site")

# 使用 fetchone() 方法获取单条数据. 使用 fetchall() 方法获取单条数据.
data = cursor.fetchall()

print(data[0])
sitename= data[0][2])
# 关闭数据库连接
db.close()