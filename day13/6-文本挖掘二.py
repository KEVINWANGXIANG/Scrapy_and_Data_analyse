
'''
更改词频

'''
import jieba
import jieba.posseg
import jieba.analyse

# sentence = "我喜欢上海东方明珠"
# w7 = jieba.cut(sentence, cut_all=True)
# for item in w7:
#     print(item)
# print("-------------------------")
# jieba.suggest_freq("上海东方", True)
# w8 = jieba.cut(sentence)
# for item in w8:
#     print(item)
#
# print("-------------------------")
#
# sentence2 = "我喜欢上海东方明珠"
# tag = jieba.analyse.extract_tags(sentence2, 2)
# print(tag)
# print("-------------------------------")
# #返回词语的位置
# w9 = jieba.tokenize(sentence2)
# for item in w9:
#     print(item)
# print("--------------------")
# w10=jieba.tokenize(sentence2, mode="search")
# for item in w10:
#     print(item)

#分析盗墓笔记的词频
data = open('C:/Users/Administrator/Desktop/盗墓笔记.txt', "rb").read()
tag = jieba.analyse.extract_tags(data, 21)
print(tag)



























