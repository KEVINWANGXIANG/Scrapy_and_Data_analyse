import numpy


class Bayes(object):
    def __init__(self):
        self.length = -1
        self.labelCount = dict()
        self.vectorCount = dict()
     #训练的方法
    def fit(self, dataSet: list, labels: list):
        if len(dataSet) != len(labels):
            raise ValueError("您输入的测试数组和类别数组长度不一致")
        #测试数据特征值的长度
        self.length = len(dataSet[0])
        #所有类别的数量
        labelsNum = len(labels)
        #去重, 不重复类别的数量
        norLabels = set(labels)
        for item in norLabels:
            thisLabel = item
            #当前类别占总数的比例
            labelCount[thisLabel] = labels.count(thisLabel) / labelsNum
        for vector, label in zip(dataSet, labels):
            if label not in vectorCount:
                self.vectorCount[label] = []
            self.vectorCount[label].append(vector)
        print("训练结束")
        return self
    def test(self, testData, labelSet):
        if self.length == -1:
            raise ValueError("您还没有进行训练，请先训练")
        #计算testData分别为各个类别的概率
        lbDict = dict()
        for thislb in labelSet:
            p = 1
            alllabel = self.labelCount[thislb]
            allVector = self.vectorCount[thislb]
            vnum = len(allVector)
            allVector = numpy.array(allVector).T
            for index in range(0, len(testData)):
                vector = list(allVector[index])
                p *= vector.count(testData[index]) / vnum
            lbDict[thislb] = p * alllabel
        thisLabel = sorted(lbDict, key=lambda x: lbDict[x], reverse=True)[0]
        return thisLabel

by1 = Bayes()






























































































