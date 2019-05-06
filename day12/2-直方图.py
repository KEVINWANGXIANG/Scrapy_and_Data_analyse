import matplotlib.pylab
import numpy



data3 = numpy.random.normal(10.0, 1.0, 10000)
# print(data3)
# matplotlib.pylab.hist(data3)#(数据)
# matplotlib.pylab.show()

data4 = numpy.random.random_integers(1, 20, 1000)
# matplotlib.pylab.hist(data4)
sty = numpy.arange(1, 30, 2)
# matplotlib.pylab.hist(data4, sty, histtype='stepfilled')
# matplotlib.pylab.show()

#子图
# matplotlib.pylab.subplot(2, 2, 3)#(行，列，当前区域)
# matplotlib.pylab.show()

matplotlib.pylab.subplot(2, 2, 1)
x1 = [1, 2, 3, 4, 5]
y1 = [5, 3, 5, 2, 1]
matplotlib.pylab.plot(x1, y1)

matplotlib.pylab.subplot(2, 2, 2)
x2 = [1, 2, 3, 4, 5]
y2 = [5, 3, 5, 2, 1]
matplotlib.pylab.plot(x1, y1, 'or')

matplotlib.pylab.subplot(2, 1, 2)
sty = numpy.arange(1, 30, 2)
matplotlib.pylab.hist(data4, sty, histtype='stepfilled')


matplotlib.pylab.show()












