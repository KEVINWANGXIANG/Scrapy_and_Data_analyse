'''
离散化：
1.等宽离散化
2.等频率离散化 ：将相同数量的记录放进一个区间里面
3.一维聚类离散化：


'''
import numpy
import pymysql
import pandas
import matplotlib.pylab
import math

conn = pymysql.connect(host="127.0.0.1", port=33061, user="root", passwd="xiangzong30917", db="houseinfo")
sql="select housesize, price from house"
data = pandas.read_sql(sql, con=conn)
#连续型数据离散化

#等宽离散化
data5=data[u"price"].copy()
data6=data5.T
data7=data6.values
# print(data7)
k = 3
# print(pandas.cut(data7, k, labels=["便宜", "适中", "昂贵"]))
# abc = [1, 5, 7, 8, 10]
print(pandas.cut(data7, [0, 5000, 10000, 15000, 20000, 25000, data7.max()]))
#等宽
# print(pandas.cut(abc, 3, labels=["便宜", "适中", "昂贵"]))
#非等宽
# print(pandas.cut(abc, [3, 6, 10, 19], labels=["便宜", "适中", "昂贵"]))

































