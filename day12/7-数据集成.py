
import numpy

a = numpy.array([[1, 5, 6], [9, 4, 3]])
b = numpy.array([[6, 36, 7], [2, 3, 39]])

c = numpy.concatenate((a, b))
print(c)
