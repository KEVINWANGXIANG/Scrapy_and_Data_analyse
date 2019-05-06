
'''
属性构造
'''
import numpy
import pymysql
import pandas
import matplotlib.pylab
import math

conn=pymysql.connect(host='127.0.0.1', user="root", port=33061, passwd="xiangzong30917", db="houseinfo")
sql="select * from house"
data8 = pandas.read_sql(sql, conn)
# print(data8)
ch = data8["price"] / data8["housesize"]
# print(ch)
data8[u"price/m^2"] = ch
# print(data8.columns)
# print(data8)
print(type(data8))
file = r'C:\Users\Administrator\Desktop\文件\000005.csv'
data8.to_csv(file, index=True, encoding="utf_8_sig")