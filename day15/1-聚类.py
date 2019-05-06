'''
聚类算法：
kmeans算法
k中心点算法

聚类三法：
1.划分法（分裂法）-->kmeans法
2.层次分析法
3.密度分析法
------------
4.网格法
5.模型法

kmeans算法：
1.随机选择k个点（k个类）作为聚类中心
2.计算各个点到这k个点的距离
3.将对应的点聚到与它最近的这个聚类中心
4.重新计算聚类中心
5.比较当前聚类中心与前一次聚类中心，如果是同一个点，得到聚类结果，若为不同的点则重复第二到五

'''
#kmeans算法
'''
#通过程序实现录取学生的聚类
import pandas
import numpy
import matplotlib.pylab as pyl

fname = open('C:/Users/Administrator/Desktop/文件/luqu.csv')
dataf = pandas.read_csv(fname)
# print(dataf)
x = dataf.iloc[:, 1:4].as_matrix()
# print(x)
from sklearn.cluster import Birch
from sklearn.cluster import KMeans
kms = KMeans(n_clusters=3, n_jobs=2, max_iter=500)
y = kms.fit_predict(x)
# dataf["class"] = y
print(y)
# print(dataf)

#可视化 x代表学生序号，y代表学生类别
s = numpy.arange(0, len(y))
# print(s)
pyl.plot(s, y, 'o')
pyl.show()
'''


#通过程序实现租房信息的聚类

import pymysql
import pandas
import numpy
import matplotlib.pylab as pyl

conn = pymysql.connect(host="127.0.0.1", port=33061, user="root", passwd="xiangzong30917", db="houseinfo")
sql = "select housesize, price from house limit 120"
dataf = pandas.read_sql(sql, conn)
# print(dataf)
x = dataf.iloc[:, :].as_matrix()

from sklearn.cluster import Birch
from sklearn.cluster import KMeans
kms = KMeans(n_clusters=3, n_jobs=2, max_iter=500)
y = kms.fit_predict(x)
print(y)
for i in range(0, len(y)):
    if y[i] == 0:
        pyl.plot(dataf.iloc[i:i + 1, 0:1].as_matrix(), dataf.iloc[i:i + 1, 1:2].as_matrix(), 'or')
    elif y[i] == 1:
        pyl.plot(dataf.iloc[i:i + 1, 0:1].as_matrix(), dataf.iloc[i:i + 1, 1:2].as_matrix(), 'p')
    else:
        pyl.plot(dataf.iloc[i:i + 1, 0:1].as_matrix(), dataf.iloc[i:i + 1, 1:2].as_matrix(), 'ok')

pyl.show()






























































































































