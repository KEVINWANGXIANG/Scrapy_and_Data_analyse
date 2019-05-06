#TF IDF算法  doc2bow

'''
相似度分析步骤：
1.读取要计算的文档
2.对文档进行分词
3.对文档进行整理成指定格式，方便后续的计算。
4.计算出词语的频率。
5.[可选]对频率低的词语进行过滤的操作
6.通过语料库建立词典
7.加载要对比的文档
8.将要对比的文档通过doc2bow转化成稀疏向量
9.对稀疏向量进行进一步处理，得到新语料库
10.将新语料库通过tfidf模型进行处理，得到tfidfs的值
11.通过token2id得到特征数
12.稀疏矩阵相似度，从而建立索引
13.得到最终相似度结果
'''
from gensim import corpora, models, similarities
import jieba
from collections import defaultdict

doc1 = r'C:/Users/Administrator/Desktop/d1.txt'
doc2 = r'C:/Users/Administrator/Desktop/d2.txt'
d1 = open(doc1).read()
d2 = open(doc2).read()
data1 = jieba.cut(d1)
data2 = jieba.cut(d2)
data11 = ""
#整理词语格式： 词语1 词语2 词语3
for item in data1:
    data11 += item + " "
data21 = ""
for item in data2:
    data21 += item + " "
documents = [data11, data21]
texts = [[word for word in document.split()] for document in documents]
frequency = defaultdict(int)
for text in texts:
    for token in text:
        frequency[token] += 1
# print(frequency)
texts = [[word for word in text if frequency[token] > 10] for text in texts]
#通过语料库建立词典
dictionary = corpora.Dictionary(texts)
dictionary.save(r'C:/Users/Administrator/Desktop/dictionary.txt')

doc3 = r'C:/Users/Administrator/Desktop/d3.txt'
d3 = open(doc3).read()
data3 = jieba.cut(d3)
data31 = ""
for item in data3:
    data31 += item + " "
new_doc = data31
#稀疏矩阵
new_vec = dictionary.doc2bow(new_doc.split())
#新的语料库
corpus = [dictionary.doc2bow(text) for text in texts]

tfidf = models.TfidfModel(corpus)
featureNum = len(dictionary.token2id.keys())
index = similarities.SparseMatrixSimilarity(tfidf[corpus], num_features=featureNum)
sim = index[tfidf[new_vec]]
print(sim)





























































































