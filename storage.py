import pymysql
import configparser
db = pymysql.connect(host="127.0.0.1",user="pmsapp",password="123456aaa",database="pms")
cursor = db.cursor()
cursor.execute("select version()")
data = cursor.fetchone()
print("database version is %s" %data)
print(cursor.description)
db.close    