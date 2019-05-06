
import matplotlib.pylab
import numpy

#折线图/散点图plot

x = [1, 2, 3, 4, 8]
y = [5, 7, 2, 1, 5]
# matplotlib.pylab.plot(x, y)#plot(x轴数据，y轴数据，展现形式)
# matplotlib.pylab.plot(x, y, 'o')
#设置颜色 c-cyan青色, r-red, m-magente品红, g-green, b-blue, y-yellow, k-black, w-white
# matplotlib.pylab.plot(x, y, 'or')
# matplotlib.pylab.show()
#设置不同的线条样式
#-普通直线， --虚线， -. -.形式， ：细小的虚线
# matplotlib.pylab.plot(x, y, '-.')
# matplotlib.pylab.show()

#散点图中点的样式
#s 方形， h 六角形， H 六角形， * 星形， + 加号， x x形， d/D 菱形, p 五角形
# matplotlib.pylab.plot(x, y, 'D')
# matplotlib.pylab.show()


#加标题,x,y轴名字
# matplotlib.pylab.plot(x, y)
# x2=[1, 3, 6, 8, 10, 12, 19]
# y2=[1, 6, 9, 10, 19, 23, 35]
# matplotlib.pylab.plot(x2, y2)
# matplotlib.pylab.title("show")
# matplotlib.pylab.xlabel("ages")
# matplotlib.pylab.ylabel("temp")
# matplotlib.pylab.xlim(0, 20)
# matplotlib.pylab.ylim(0, 40)
# matplotlib.pylab.show()


#生成随机数
data=numpy.random.random_integers(1, 20, 10)#(最小值，最大值，个数)
# print(data)
data2=numpy.random.normal(5.0, 2.0, 10)#(均数, 西格玛, 个数)
print(data2)



# 直方图hist

