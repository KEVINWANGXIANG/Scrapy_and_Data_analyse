
#导入csv数据
import pandas

f=open("C:/Users/Administrator/Desktop/文件/000002.csv")
i = pandas.read_csv(f)
print(i)
# print(i.describe())
#降序
print(i.sort_values(by="评论数", ascending=False))

