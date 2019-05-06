import matplotlib.pylab
import numpy
import pandas
import pymysql

conn = pymysql.connect(host="127.0.0.1", port=33061, user="root", passwd="xiangzong30917", db="houseinfo")
sql = "select * from house"
data = pandas.read_sql(sql, con=conn)
# print(data)

#分布分析
#极差:最大值-最小值
#组距：极差/组数
da2=data.values.T
priceMax = da2[2].max()
priceMin = da2[2].min()
housesizeMax = da2[1].max()
housesizeMin = da2[1].min()
priceRg = priceMax - priceMin
housesizeRg = housesizeMax - housesizeMin

priceDst = priceRg / 12
housesizeDst = housesizeRg / 12

#画价格的直方图
priceSty = numpy.arange(priceMin, priceMax, priceDst)
matplotlib.pylab.hist(da2[2], priceSty, histtype='stepfilled')
matplotlib.pylab.show()

#画评论的直方图
housesizeSty = numpy.arange(housesizeMin, housesizeMax, housesizeDst)
# matplotlib.pylab.hist(da2[1], housesizeSty, histtype='stepfilled')
# matplotlib.pylab.show()

matplotlib.pylab.plot(da2[1], da2[2], 'or')
matplotlib.pylab.show()





























































