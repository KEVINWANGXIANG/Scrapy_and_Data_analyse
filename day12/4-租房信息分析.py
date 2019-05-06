import matplotlib.pylab
import numpy
import pandas
import pymysql

conn = pymysql.connect(host="127.0.0.1", port=33061, user="root", passwd="xiangzong30917", db="houseinfo")
housesize = pandas.read_sql("select housesize from house", con=conn)
price=pandas.read_sql("select price from house", con=conn)

matplotlib.pylab.subplot(2, 2, 1)
matplotlib.pylab.plot(housesize, price)

matplotlib.pylab.subplot(2, 2, 2)
matplotlib.pylab.plot(housesize, price, 'or')

matplotlib.pylab.subplot(2, 1, 2)
matplotlib.pylab.hist(housesize)

matplotlib.pylab.title("House")
matplotlib.pylab.xlabel("housesize")
matplotlib.pylab.ylabel("price")

matplotlib.pylab.show()















