import pandas as pd
import numpy as np
import matplotlib.pylab as ply

fname = open(r'C:/Users/Administrator/Desktop/lianjia.csv')
df = pd.read_csv(fname)
# print(type(df))
# print(df[:3])
# print(df[u'Direction'][:3])
# print(df[u'Direction'][:3].as_matrix())
#相同数据出现的频率
counts = df[u'Direction'].value_counts()
# print(counts)
# print(type(counts))

# plt = counts.plot(kind='bar').get_figure()
# plt.savefig(r'C:/Users/Administrator/Desktop/plot.png')

print("----------------------------------------")
good = df[df["Size"] > 500]
# print(good)
print(good[:3])

year_counts = good["Size"].value_counts()
print(year_counts)
# print(type(year_counts))
# print(year_counts.index)
# print(year_counts.values)
# print(type(year_counts.index))
# x = year_counts.index
# x = list(numpy.array(x))
# y = year_counts.values
# y = list(numpy.array(y))
#
# print(x)
# print(y)
# ply.plot(x, y, 'o')
# ply.show()
# print(df)

rate = df["Price"] / df["Size"]
print(rate[:5])

print("------------------------------")
#数据分组
df = pd.DataFrame({'A': ['foo', 'bar', 'foo', 'bar', 'foo', 'bar', 'foo', 'bar'],
                   'B': ['one', 'one', 'two', 'three', 'two', 'two', 'one', 'three'],
                   'C': np.random.randn(8),
                   'D': np.random.randn(8)})
print(df)

grouped = df.groupby('A')
print(grouped.first())

grouped = df.groupby(['A', 'B'])
print(grouped.first())
print(grouped.last())

def get_type(letter):
    if letter.lower() in "abem":
        return 'vowel'
    else:
        return 'consonant'
grouped = df.groupby(get_type, axis=1)
print(grouped.first())

































