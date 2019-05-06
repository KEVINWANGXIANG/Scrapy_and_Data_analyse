'''
（关联算法）
Apriori算法的实现：
1.阈值：最小支持度，最小置信度
2.计算支持度Support(A=>B)=(A与B同时发生的数量)/时间总数量和置信度=Support_count(A and B)/Total(A)
置信度：Confidence(A=>B)=p(B|A)=Support(A and B)/p(A)=Support_count(A and B)/Support(A)
3.筛选
4.继续计算

'''

#学员购买课程的关联
from apriori import *
import pandas

fileName = open('C:/Users/Administrator/Desktop/文件/lesson_buy.csv')
dataFrame = pandas.read_csv(fileName, header=None)
# print(dataFrame)
#转化数据
change = lambda x: pandas.Series(1, index=x[pandas.notnull(x)])
mapok = map(change, dataFrame.as_matrix())
data = pandas.DataFrame(list(mapok)).fillna(0)
# print(data)
#设置临界支持度、置信度设置
support = 0.1 #同时发生的概率
confidence = 0.3  #在A发生的情况下，B发生的概率
find_rule(data, support, confidence, "-->")









































































