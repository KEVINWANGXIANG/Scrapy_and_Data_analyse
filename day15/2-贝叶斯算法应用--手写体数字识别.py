#贝叶斯算法的应用
from numpy import *
import numpy
from os import listdir


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
            self.labelCount[thisLabel] = labels.count(thisLabel) / labelsNum
        for vector, label in zip(dataSet, labels):
            # print(vector, label)
            if label not in self.vectorCount:
                self.vectorCount[label] = []
            self.vectorCount[label].append(vector)
            # pass
        print("训练结束")
        return self
    def btest(self, testData, labelSet):
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

#步骤1：加载数据
def dataToArray(fname):
    arr=[]
    fh = open(fname)
    for i in range(0, 32):
        thisline = fh.readline()
        for j in range(0, 32):
            arr.append(int(thisline[j]))
    return arr

# arr1=dataToArray(r'C:/Users/Administrator/Desktop/weixin.txt')
# print(arr1)
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
bys = Bayes()
trainData, labels = trainData()
bys.fit(trainData, labels)

#单个手写体数字测试
thisData = dataToArray('C:/Users/Administrator/Desktop/digits/digits/testdata/8_21.txt')
labelsAll = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
rst = bys.btest(thisData, labelsAll)
print(rst)


'''
#识别多个手写体数字（批量测试）
testFileAll = listdir('C:/Users/Ad ministrator/Desktop/digits/digits/testdata')
allFileNum = len(testFileAll)
num = len(testFileAll)
errNum = 0
for i in range(0, num):
    thisFileName = testFileAll[i]
    print(thisFileName)
    trueNum = sepLabel(thisFileName)
    thisData = dataToArray('C:/Users/Administrator/Desktop/digits/digits/testdata/' + thisFileName)
    rst = bys.btest(thisData, labelsAll)
    print("该数字是:" + str(trueNum) + ",识别的数字是:" + str(rst))
    if rst != trueNum:
        errNum += 1

rightRate = float(errNum) / float(allFileNum)
print("正确率是:" + rightRate)
'''

















































































































































