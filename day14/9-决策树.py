
'''
决策树算法：
1.ID3
2.C4.5
3.CART
'''
import pandas


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
        y[i] = int(-1)

# print(y)
#容易错的地方:直接输入训练
#正确的做法：转化好格式，将x和y转化为数据框，然后再转化为数组并指定格式
xf = pandas.DataFrame(x)
yf = pandas.DataFrame(y)
x2 = xf.as_matrix().astype(int)
y2 = yf.as_matrix().astype(int)
# print(x2)
# print(y2)
#建立决策树
from sklearn.tree import DecisionTreeClassifier as DTC

dtc = DTC(criterion="entropy")
dtc.fit(x2, y2)
#直接预测
import numpy

x3 = numpy.array([[1, -1, -1, 1], [1, 1, 1, 1], [-1, -1, 1, 1], [1, -1, 1, -1]])
result = dtc.predict(x3)
print(result)

#决策树可视化
from sklearn.tree import export_graphviz
# from sklearn.externals import StringIO

# with open("C:/Users/Administrator/Desktop/dtc.dot", "w") as file:
#     export_graphviz(dtc, feature_names=["Combat", "NumCourse", "Promotion", "Doc"], out_file=file)































