from sklearn import *
import sklearn
import pandas
import numpy
from sklearn.linear_model import LogisticRegression as LR
from sklearn.linear_model import RandomizedLogisticRegression as RLR
#逻辑回归
'''
1的概率：p
0的概率1-p
概率比=p/(1-p)
z = logic(p)=ln(p/(1-p))
p = 1/(1+e**(-z)) 逻辑函数
'''

#逻辑回归
fname = open('C:/Users/Administrator/Desktop/文件/回归算法数据.csv')
dataf = pandas.read_csv(fname)
#逗号隔开，前面为行，后面是列,as_matrix转为数组
x = dataf.iloc[:, 1:4].as_matrix()
y = dataf.iloc[:, 0:1].as_matrix()
# print(x)
# print("------")
# print(y)
r1 = RLR()
r1.fit(x, y)
r1.get_support(indices=True) #特征筛选
t = dataf[dataf.columns[r1.get_support(indices=True)]].as_matrix()
r2 = LR()
r2.fit(t, y)
print("训练结束")
print(str(r2.score(x, y)))
# print("模型正确率为:" + r2.score(x, y))

import numpy as np
import matplotlib.pyplot as plt
# .T是转置，dot是矩阵乘法
X = 2*np.random.rand(100,1)
y = 4+3*X + np.random.randn(X.shape[0], X.shape[1])
X_b = np.c_[np.ones(X.shape), X]
theta_best = np.linalg.inv( X_b.T.dot( X_b ) ).dot( X_b.T ).dot(y)
print( theta_best )
X_new = np.array([[0], [2]])
X_new_b = np.c_[np.ones((2,1)), X_new]
y_predict = X_new_b.dot( theta_best )
plt.plot( X, y, 'r.' )
plt.plot( X_new, y_predict, 'b-' )
plt.show()



'''
import numpy as np
import matplotlib.pyplot as plt
#设置
x = np.array([1., 2., 3., 4., 5.])
y = np.array([1., 3., 2., 3., 5.])
# fname = open('C:/Users/Administrator/Desktop/文件/回归算法数据.csv')
# dataf = pandas.read_csv(fname)
# x = dataf.iloc[:, 1:2].as_matrix()
# y = dataf.iloc[:, 2:3].as_matrix()
# x = [i for item in x for i in item]
# y = [i for item in y for i in item]
# x = np.array(x)
# y = np.array(y)

print(x)
print(y)

##接下来按照公式求解即可
x_mean = np.mean(x)
y_mean = np.mean(y)
num = 0.0
d = 0.0
for x_i, y_i in zip(x, y):
    num += (x_i - x_mean) * (y_i - y_mean)
    d += (x_i - x_mean) ** 2
##所解值
a = num / d
b = y_mean - a * x_mean
y_hat = a * x + b
##绘图
plt.scatter(x, y)
plt.plot(x, y_hat, color='r')

plt.show()
'''































