
import jieba
#词性标注
import jieba.posseg
sentence = "我喜欢上海东方明珠"
#参数:cut_all=True全模式 False精准模式
w1 = jieba.cut(sentence, cut_all=True)
for item in w1:
    print(item)
print("--------------------------")
w2 = jieba.cut(sentence, cut_all=False)
for item in w2:
    print(item)
print("---------------------------")
#搜索引擎模式
w3 = jieba.cut_for_search(sentence)
for item in w3:
    print(item)
print("---------------------------")
#同精准模式，默认使用精准模式
w4=jieba.cut(sentence)
for item in w4:
    print(item)
print("---------------------------")
#词性标注
w5 = jieba.posseg.cut(sentence)
#.flag词性 .word词语
# a:形容词 c:连词 d:副词 e:叹词 f:方位词 i:成语 m:数词 n:名词 nr:人名
# ns:地名 nt:机构团体 nz:其他专有名词 p:介词 r:代词 t:时间 u:助词 v:动词
# vn:动名词 w:标点符号 un:未知词语
for item in w5:
    print(item.word + "---" + item.flag)
print("---------------------------")
sentence2 = "天善智能是一个非常好的机构"
w6=jieba.posseg.cut(sentence2)
for item in w6:
    print(item.word + "---" + item.flag)

print("---------------------------")
#添加自己的词库
#词典加载
jieba.load_userdict("C:/Users/Administrator/AppData/Local/Programs/Python/Python36-32/Lib/site-packages/jieba/dict2.txt")
sentence3 = "重庆韬翔有限责任公司是一个非常差的公司"
w7=jieba.posseg.cut(sentence3)
for item in w7:
    print(item.word + "---" + item.flag)




































