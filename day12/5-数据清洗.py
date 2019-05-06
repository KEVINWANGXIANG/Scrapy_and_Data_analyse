'''
步骤：
1.缺失值处理（通过describe与len直接发现、通过0数据发现）
2.异常值处理（通过散点图发现）
'''

#数据清洗
#发现缺失值
import pymysql
import numpy
import pandas
import matplotlib.pylab

conn = pymysql.connect(host="127.0.0.1", port=33061, user="root", passwd="xiangzong30917", db="houseinfo")
sql = "select * from house"
data = pandas.read_sql(sql, con=conn)
# print(data)

# print(data.describe())
# print(len(data))

x = 0
'''
data["price"][(data["price"] == 0)] = None
for i in data.columns:
    for j in range(len(data)):
        if (data[i].isnull())[j]:
            data[i][j] = "5000"
            x += 1
'''
# print(x)
# print(data)

#异常值处理
#画散点图,横轴是housesize，纵轴为price
data["housesize"][(data["housesize"] == 0)] = None
for i in data.columns:
    for j in range(len(data)):
        if (data[i].isnull())[j]:
            print(data[i][j])
            data[i][j] = "60"
            x += 1
print(x)
y=0
data["price"][(data["price"] == 0)] = None
for i in data.columns:
    for j in range(len(data)):
        if (data[i].isnull())[j]:
            data[i][j] = "5000"
            y += 1
print(y)

data["price"][(data["price"] > 25000)] = None
for i in data.columns:
    for j in range(len(data)):
        if (data[i].isnull())[j]:
            data[i][j] = "12345"
            # y += 1


# print(data["price"])

# print(data.values)
#异常值处理
#housesize>80,price>100000为异常
# line = len(data.values)
# col=len(data.values[0])
# da=data.values
# for i in range(0, line):
#     for j in range(0, col):
#         if da[i][1]>80:
#             # print(da[i][j])
#             da[i][1]=36
a = 0
line = len(data.values)
col = len(data.values[0])
data = data.values
for i in range(0, line):
    for j in range(1, col - 1):
        if data[i][j + 1] / data[i][j] > 1000:
            a += 1

print(a)





# da = da.T
# housesize=da[1]
# price=da[2]
# print(data)
# print(data["price"])

# data2=data.values.T
# housesize=data2[1]
# price=data2[2]
# matplotlib.pylab.plot(housesize, price, 'or')
# matplotlib.pylab.show()

# housesize=data["housesize"]
# price=data["price"]
# matplotlib.pylab.plot(housesize, price, 'or')
# matplotlib.pylab.show()


























