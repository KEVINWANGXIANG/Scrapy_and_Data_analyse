from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
import numpy as np

# iris = load_iris()
# # print(iris)
# data = iris.data[0:100, [0, 2]]
# print(data)
# target = iris.target[0:100]
# # print(target)

from math import log
import operator
import pandas

def calcShannonEnt(dataSet):  # 计算数据的熵(entropy)
    numEntries=len(dataSet)  # 数据条数
    labelCounts={}
    for featVec in dataSet:
        currentLabel=featVec[-1]# 每行数据的最后一个字（类别）
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel] = 0
        labelCounts[currentLabel] += 1  # 统计有多少个类以及每个类的数量
    shannonEnt = 0
    for key in labelCounts:
        prob = float(labelCounts[key]) / numEntries # 计算单个类的熵值
        shannonEnt -= prob * log(prob, 2)# 累加每个类的熵值
    return shannonEnt

def createDataSet1(path):    # 创造示例数据
    fname = open(path)
    dataf = pandas.read_csv(fname)
    dataSet = dataf.iloc[:, 1:len(dataf.columns)].as_matrix()
    dataSet = list(dataSet)
    b = []
    for i in range(len(dataSet)):
        b.append(list(dataSet[i]))
    columns = dataf.columns
    columns = list(columns)
    labels = columns[1:len(columns)]
    return b, labels

def splitDataSet(dataSet, axis, value):# 按某个特征分类后的数据
    retDataSet = []
    for featVec in dataSet:
        if featVec[axis] == value:
            reducedFeatVec = featVec[:axis]
            reducedFeatVec.extend(featVec[axis + 1:])
            retDataSet.append(reducedFeatVec)
    return retDataSet

def chooseBestFeatureToSplit(dataSet):  # 选择最优的分类特征
    numFeatures = len(dataSet[0])-1
    baseEntropy = calcShannonEnt(dataSet)  # 原始的熵
    bestInfoGain = 0
    bestFeature = -1
    for i in range(numFeatures):
        featList = [example[i] for example in dataSet]
        uniqueVals = set(featList)
        newEntropy = 0
        for value in uniqueVals:
            subDataSet = splitDataSet(dataSet, i, value)
            prob = len(subDataSet) / float(len(dataSet))
            newEntropy += prob * calcShannonEnt(subDataSet)  # 按特征分类后的熵
        infoGain = baseEntropy - newEntropy  # 原始熵与按特征分类后的熵的差值
        if (infoGain > bestInfoGain):   # 若按某特征划分后，熵值减少的最大，则此特征为最优分类特征
            bestInfoGain = infoGain
            bestFeature = i
    return bestFeature

def majorityCnt(classList):    #按分类后类别数量排序，比如：最后分类为2男1女，则判定为男；
    classCount={}
    for vote in classList:
        if vote not in classCount.keys():
            classCount[vote] = 0
        classCount[vote] += 1
    sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]

def createTree(dataSet, labels):
    classList = [example[-1] for example in dataSet]  # 类别：男或女
    if classList.count(classList[0]) == len(classList):
        return classList[0]
    if len(dataSet[0]) == 1:
        return majorityCnt(classList)
    bestFeat = chooseBestFeatureToSplit(dataSet)#选择最优特征
    bestFeatLabel = labels[bestFeat]
    myTree = {bestFeatLabel: {}} #分类结果以字典形式保存
    del(labels[bestFeat])
    featValues = [example[bestFeat] for example in dataSet]
    uniqueVals = set(featValues)
    for value in uniqueVals:
        subLabels = labels[:]
        myTree[bestFeatLabel][value] = createTree(splitDataSet(dataSet, bestFeat, value), subLabels)
    return myTree
#实用决策树进行分类
'''
def classify(inputTree, featLabels, testVec):
    global classLabel
    # classLabel = None
    firstStr = list(inputTree.keys())[0]
    secondDict = inputTree[firstStr]
    featIndex = featLabels.index(firstStr)
    for key in secondDict.keys():
        if testVec[featIndex] == key:
            if type(secondDict[key]).__name__ == 'dict':
                classLabel = classify(secondDict[key], featLabels, testVec)
            else:
                classLabel = secondDict[key]
    return classLabel
'''
def classify(input_tree, feat_labels, test_vec):
    """
    决策树分类
    :param input_tree: 决策树
    :param feat_labels: 特征标签
    :param test_vec: 测试的数据
    :return:
    """
    first_str = list(input_tree.keys())[0]  # 获取树的第一特征属性
    second_dict = input_tree[first_str]  # 树的分子，子集合Dict
    feat_index = feat_labels.index(first_str)  # 获取决策树第一层在feat_labels中的位置
    for key in second_dict.keys():
        if test_vec[feat_index] == key:
            if type(second_dict[key]).__name__ == 'dict':
                class_label = classify(second_dict[key], feat_labels, test_vec)
            else:
                class_label = second_dict[key]
            return class_label


if __name__ == '__main__':
    dataSet, labels = createDataSet1('C:/Users/Administrator/Desktop/文件/lesson1.csv')  # 创造示列数据
    labelsNew = []
    for i in range(len(labels) - 1):
        labelsNew.append(labels[i])
    tree = createTree(dataSet, labelsNew)
    print(tree)
    label = classify(tree, ["实战", "课时数", "是否促销", "是否提供资源"], ["是", "少", "是", "否"])
    print(label)
