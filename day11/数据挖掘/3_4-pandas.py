import pandas as pd
import numpy as np
import pandas.util.testing as tm

colors = tm.np.random.choice(['red', 'green'], size=10)
foods = tm.np.random.choice(['eggs', 'ham'], size=10)

index = pd.MultiIndex.from_arrays([colors, foods], names=['color1', 'food1'])
df = pd.DataFrame(np.random.randn(10, 2), index=index)
df.columns = ['a', 'b']
print(df)

df['c'] = pd.Series(np.random.rand(10), index=df.index)
print(df)
df.insert(1, 'e', df['a'])
print(df)

del df['c']
print(df)

df2 = df.drop(['a', 'b'], axis=1)
print(df2)
print(df)

b = df.pop('b')
df.insert(0, 'b', b)
print(df)
print("-----------------字符串操作--------------")
s = pd.Series(list("ABCDEF"))
print(s)
print(s.str.lower())
print(s.str.upper())
print(s.str.len())

s2 = pd.Series(['a_b_c', 'c_a_b', np.nan, 'f_g_h'])
# s2 = s2.str.split("_")
# print(s2.str.len())

print(s2.str.split("_").str.get(1))
print(s2.str.split("_").get(1))
#以a开头或是以b结尾的用X代替
print(s2.str.replace("^a|b$", "X", case=False))
print("-----------------字符串提取数据--------------")
s = pd.Series(['a1', 'a2', 'b1', 'b2', 'c3', 'c'])
print(s)
print(s.str.extract('[ab]([\d])'))
print(s.str.extract('([abc])([\d])'))
print(s.str.extract('([abc])(\d)?'))
print(s.str.extract('(?P<letter>[abc])(?P<digit>\d)'))
print("-------------匹配字符串------------")
s = pd.Series(['a1', 'A2', 'b1', 'ab2', 'c3', 'abd', 'a2c', np.nan, 'a1b'])
print(s)
pattern = r'[a-z][0-9]'
print(s.str.contains(pattern))
print(s.str.contains(pattern, na=False))

print(s.str.match(pattern, as_indexer=False))
print(s.str.startswith('a', na=False))
print(s.str.contains('^a', na=False))
print(s.str.endswith('1', na=False))
print(s.str.contains('1$', na=False))
print("-------------广播-----------")
df = pd.DataFrame({'one': pd.Series(np.random.randn(4), index=list('abcd'))})
df['two'] = 1
df['thr'] = 2
print(df)
row = df.ix[1]
print(row)
column = df['two']
print(column)
#将df中的每一行与row做减法
print(df.sub(row, axis='columns'))
print("--------------带有缺失值的计算----------------")
print(df)
df1 = pd.DataFrame(np.random.randn(5, 3), index=list("abcde"), columns=["one", 'two', 'three'])
df1.ix[1, :-1] = np.nan
print(df1)
df2 = pd.DataFrame(np.random.randn(5, 3), index=list("abcde"), columns=['one', 'two', 'three'])
print(df2)
print(df1 + df2)
print(df1["one"].sum())
print(df1.mean())

print("--------------填充缺失值-------------")
df1 = pd.DataFrame(np.random.randn(5, 3), index=list("abcde"), columns=["one", 'two', 'three'])
df1.ix[1, :-1] = np.nan
df1.ix[1:-1, 2] = np.nan
print(df1)
# print(df1.fillna(0))
# print(df1.fillna("missing"))
# print(df1.fillna(method='pad'))
# print(df1.fillna(df1.mean()))
print(df1.fillna(df1.mean()['one':'two']))






