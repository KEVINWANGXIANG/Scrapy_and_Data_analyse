#BP人工神经网络的实现
'''
实现步骤：
1.读取数据
2.keras.models Sequential(建立模型)  /keras.layers.core  Dense(建立层)  Activation(设置激活函数)
3.建立模型 Sequential
4.Dense建立层
5.Activation激活函数
6.模型编译compile
7.fit训练学习
8.验证(测试，分类预测)
'''
#预测课程销量
import pandas

#数据的读取和整理
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
model.add(Dense(10, input_dim=len(x2[0])))
model.add(Activation("relu"))
#输出层
model.add(Dense(1, input_dim=1))
model.add(Activation("sigmoid"))
#模型的编译
model.compile(loss="binary_crossentropy", optimizer="adam", class_mode="binary")
#训练
model.fit(x2, y2, nb_epoch=1000, batch_size=100)
#预测分类
rst = model.predict_classes(x).reshape(len(x))
# print(rst)
x = 0
for i in range(0, len(x2)):
    if rst[i] != y[i]:
        x += 1
print(1 - x / len(x2))


































































