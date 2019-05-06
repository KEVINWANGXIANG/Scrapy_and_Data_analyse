'''

常见的函数变换包括：开方，平方，对数

数据规范化：
1.离差标准化(最小最大标准化)--消除量纲（单位）影响以及编变异大小因素的影响  x1=(x-min)/(max-min)
2.标准差标准化（零-均值标准化）--消除单位影响以及变量自身变异影响 x1=(x-平均数)/标准差
3.小数定标规范化--消除单位影响 x1=x/10^k  k=log10(x的绝对值的最大值)


'''
import numpy
import pymysql
import pandas
import matplotlib.pylab
import math

conn = pymysql.connect(host="127.0.0.1", port=33061, user="root", passwd="xiangzong30917", db="houseinfo")
sql="select housesize, price from house"
data = pandas.read_sql(sql, con=conn)
# print(data)
# print(data.describe())
#离差标准化
data2 = (data - data.min()) / (data.max() - data.min())
# print(data2)

#标准差标准化
data3 = (data - data.mean()) / data.std()
# print(data3)

#小数定标规范化
k=numpy.log10(abs(data.max()))
k=numpy.ceil(k)
data4 = data / 10 ** k
print(data4)



























































