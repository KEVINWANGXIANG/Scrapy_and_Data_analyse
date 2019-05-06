
'''
实现步骤：
1.处理数据
2.数据向量化
3.计算欧里几得距离
4.根据距离进行分类
'''

import numpy
import operator

'''
扩展行
tile(a, (size, 1))
'''


def knn(k, testData, trainData, labels):
    #获取数组的行数
    trainDataSize = trainData.shape[0]
    #扩展并计算对应差值
    dif = tile(testData, (trainDataSize, 1)) - trainData
    sqdif = dif ** 2
    # axis=1表示按行相加 , axis=0表示按列相加
    sumSqdf = sqdif.sum(axis=1)
    distance = sumSqdf ** 0.5
    sortDistance = distance.arsort()
    count={}
    for i in range(0, k):
        vote = labels[sortDistance[i]]
        count[vote] = count.get(vote, 0) + 1
    # operator.itemgetter(1) 获取对象的第一个域的值
    sortCount = sorted(count.items(), key=operator.itemgetter(1), reverse=True)
    return sortCount[0][0]














