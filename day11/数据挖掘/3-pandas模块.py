
# import pandas as pda
import pandas

'''
Series:
#index 索引
DataFrame:

'''
a=pandas.Series([8, 9, 2, 1])
print(a[0])
b=pandas.Series([8, 9, 2, 1], index=["one", "two", "three", "four"])
print(b)

c=pandas.DataFrame([[5, 6, 2, 3], [8, 4, 6, 3], [6, 4, 31, 2]])
print(c)
print(c[0][0])
d=pandas.DataFrame([[5, 6, 2, 3], [8, 4, 6, 3], [6, 4, 31, 2]], columns=["one", "two", "three", "four"])
print(d)

e=pandas.DataFrame({
    "one": 4,
    "two": [6, 2, 3],
    "three": list(str(982))
})
print(e)
## 头部数据，默认前五行
print(d.head(2))
#尾部数据，默认是后五行
print(d.tail(2))

print(d)
#std:标准差
print(d.describe())

#转置
print(d.T)

































