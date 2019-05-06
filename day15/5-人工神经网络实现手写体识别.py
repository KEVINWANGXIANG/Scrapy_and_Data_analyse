
import pandas
from numpy import *
import numpy
import operator
from os import listdir

def dataToArray(fname):
    arr=[]
    fh = open(fname)
    for i in range(0, 32):
        thisline = fh.readline()
        for j in range(0, 32):
            arr.append(int(thisline[j]))
    return arr
def sepLabel(fname):
    fileStr = fname.split(".")[0]
    label = fileStr.split("_")[0]
    label = int(label)
    return label
#步骤2:建立训练数据集
def trainData():
    labels = []
    trainFile = listdir('C:/Users/Administrator/Desktop/digits/digits/traindata')
    num = len(trainFile)
    #长度1024列, 每一行存储一个文件
    #以一个数组存储所有训练数据，行为文件数，列为32*32=1024
    #生成一个二维数组zeros(2, 5)
    trainArr = numpy.zeros((num, 1024))
    for i in range(0, num):
        thisfName = trainFile[i]
        thisLabel = sepLabel(thisfName)
        labels.append(thisLabel)
        trainArr[i, :] = dataToArray('C:/Users/Administrator/Desktop/digits/digits/traindata/' + thisfName)
    return trainArr, labels
trainArr, labels = trainData()
tx2 = pandas.DataFrame(trainArr).as_matrix().astype(int)
ty2 = pandas.DataFrame(labels).as_matrix().astype(int)



fname = open('C:/Users/Administrator/Desktop/文件/lesson1.csv')
dataf = pandas.read_csv(fname)
# print(dataf)
x = dataf.iloc[:, 1:5].as_matrix()
# print(x)
y = dataf.iloc[:, 5].as_matrix()
# print(y)
for i in range(0, len(x)):
    for j in range(0, len(x[i])):
        thisData = x[i][j]
        if thisData == "是" or thisData == "多" or thisData == "高":
            x[i][j] = int(1)
        else:
            x[i][j] = int(-1)
for i in range(0, len(y)):
    thisData = y[i]
    if thisData == "高":
        y[i] = int(1)
    else:
        y[i] = int(0)
xf = pandas.DataFrame(x)
yf = pandas.DataFrame(y)
x2 = xf.as_matrix().astype(int)
y2 = yf.as_matrix().astype(int)

#使用人工神经网络模型
from keras.models import Sequential
from keras.layers.core import Dense, Activation

model = Sequential()
#input_dim代表的特征数
#输入层
model.add(Dense(10, input_dim=1024))
model.add(Activation("relu"))
#输出层
model.add(Dense(1, input_dim=1))
model.add(Activation("sigmoid"))
#模型的编译
model.compile(loss="mean_squared_error", optimizer="adam")
#训练
model.fit(tx2, ty2, nb_epoch=10000, batch_size=6)
#预测分类
rst = model.predict_classes(tx2).reshape(len(x))
print(rst)
x = 0
for i in range(0, len(x2)):
    if rst[i] != y[i]:
        x += 1
print(1 - x / len(x2))


































































