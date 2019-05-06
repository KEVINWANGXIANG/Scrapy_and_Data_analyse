import numpy
# import numpy as nn 别名

#创建一维数组
x = numpy.array(["a", "9", "8", "2", "abcd"])
print(x)
print(x[1])
print(type(x))

#创建二维数组
x2 = numpy.array([[5, 4, 6], [1, 2, 3], [9, 8, 7]])
print(x2)
print(x2[1][2])
print(type(x2))

#排序 sort

# x.sort()
# print(x)
# x2.sort()
# print(x2)

#取最大值和最小值
y1 = x2.max()
print(y1)

y2 = x2.min()
print(y2)

#切片
print(x[1:3])
print(x[:2])
print(x[3:])




























