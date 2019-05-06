import numpy
import pymysql
import pandas
import matplotlib.pylab

from sklearn.decomposition import PCA
#属性规约 数值规约

#主成分分析
conn = pymysql.connect(host='127.0.0.1', user="root", port=33061, passwd="xiangzong30917", db="houseinfo")
sql = "select housesize, price from house"
data8 = pandas.read_sql(sql, conn)
# print(data8)
ch = data8["price"] / data8["housesize"]
data8[u"price/m^2"] = ch
# print(ch)

# print(data8.columns)
# print(data8)
data9=data8
# print(data9)

#主成分分析进行中
pca1 = PCA()
pca1.fit(data9)
#返回模型中的各个特征量
characteristic = pca1.components_
# print(tz1)
#各个成分中各自方差百分百贡献率
rate = pca1.explained_variance_ratio_
# print(rate)

pca2 = PCA(2)
pca2.fit(data9)
reduction = pca2.transform(data9)#降维
print(reduction)
print("-------------------")
#恢复维数
print(pca2.inverse_transform(reduction))

