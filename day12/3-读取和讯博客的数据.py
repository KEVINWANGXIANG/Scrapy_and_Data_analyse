import matplotlib.pylab
import numpy
import pandas

f = open("C:/Users/Administrator/Desktop/文件/000002.csv")
data = pandas.read_csv(f)
# print(data)
# print(data.shape)
# print(data.values)
# print(data.values[0])
data2 = data.T
x1 = data2.values[1]
y1 = data2.values[2]
matplotlib.pylab.plot(x1, y1)
matplotlib.pylab.title("ratio")
matplotlib.pylab.xlabel("reading")
matplotlib.pylab.ylabel("review")
matplotlib.pylab.show()