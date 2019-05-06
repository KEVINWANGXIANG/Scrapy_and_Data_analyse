#pillow
from PIL import Image
from numpy import *
import numpy
import operator
from os import listdir

def knn(k, testData, trainData, labels):
    #获取数组的行数
    trainDataSize = trainData.shape[0]
    #扩展并计算对应差值
    dif = tile(testData, (trainDataSize, 1)) - trainData
    sqdif = dif ** 2
    # axis=1表示按行相加 , axis=0表示按列相加
    sumSqdf = sqdif.sum(axis=1)
    distance = sumSqdf ** 0.5
    sortDistance = distance.argsort()
    count={}
    for i in range(0, k):
        vote = labels[sortDistance[i]]
        count[vote] = count.get(vote, 0) + 1
    # operator.itemgetter(1) 获取对象的第一个域的值
    sortCount = sorted(count.items(), key=operator.itemgetter(1), reverse=True)
    return sortCount[0][0]

#建立一个函数取文件名的前缀
def sepLabel(fname):
    fileStr = fname.split(".")[0]
    label = fileStr.split("_")[0]
    label = int(label)
    return label

#识别图片上的数字
#步骤1：加载数据
def dataToArray(fname):
    arr = []
    fh = open(fname)
    for i in range(0, 32):
        thisline = fh.readline()
        for j in range(0, 32):
            arr.append(int(thisline[j]))
    return arr

# arr1=dataToArray(r'C:/Users/Administrator/Desktop/weixin.txt')
# print(arr1)
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

def dataTest():
    trainArr, labels = trainData()
    testList = listdir(r'C:/Users/Administrator/Desktop/digits/digits/testdata')
    tNum = len(testList)
    for i in range(0, tNum):
        thisTestFile = testList[i]
        testArr = dataToArray('C:/Users/Administrator/Desktop/digits/digits/testdata/' + thisTestFile)
        rknn = knn(3, testArr, trainArr, labels)
        print(rknn)

# dataTest()
#抽某一个测试文件出来进行试验
def singleFileTest(file):
    trainArr, labels = trainData()
    testArr = dataToArray(file)
    rknn = knn(3, testArr, trainArr, labels)
    print(rknn)
singleFileTest(r'C:/Users/Administrator/Desktop/num.txt')
def pic2txt(imgPath, txtPath):
    im = Image.open(imgPath)
    fh = open(txtPath, "a")
    for i in range(0, 32):
        for j in range(0, 32):
            cl = im.getpixel((j, i))
            clAll = cl[0] + cl[1] + cl[2]
            if clAll == 0:
                fh.write("1")
            else:
                fh.write("0")
        fh.write("\n")
    fh.close()
# txtPath = r'C:/Users/Administrator/Desktop/num.txt'
# pic2txt(r'C:/Users/Administrator/Desktop/test.png', txtPath)
# singleFileTest(txtPath)






















































