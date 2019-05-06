import pandas as pd
import numpy as np

import pandas.util.testing as tm

colors = tm.np.random.choice(['red', 'green'], size=10)
foods = tm.np.random.choice(['eggs', 'ham'], size=10)

# print(colors)
# print(foods)

index = pd.MultiIndex.from_arrays([colors, foods], names=['color1', 'food1'])
df = pd.DataFrame(np.random.randn(10, 2), index=index)
# print(df)

# print(df.query('color1 == "red"'))

grouped = df.groupby(level='food1')
# print(grouped.sum())
grouped = df.groupby(level='color1')
# print(grouped.sum())
#
# index = pd.MultiIndex.from_arrays([colors, foods], names=['color1', 'food1'])
# df = pd.DataFrame(np.random.randn(10, 2), index=index)
df.columns = ['a', 'b']
print(df)
grouped = df.groupby(level='color1')
# print(grouped.sum())
grouped_a = grouped['a']
# print(grouped_a.sum())
# print(grouped.sum())
# for name, group in grouped:
#     print(name)
#     print(group)

# for name, group in df.groupby(level=['color1', 'food1']):
#     print(name)
#     print(group)
print("------------------------------------------")
grouped = df.groupby(level=['color1', 'food1'])
print(grouped.aggregate(np.sum))
#将两个索引转化为列变量
print(grouped.aggregate(np.sum).reset_index())
#同上
print(df.groupby(level=['color1', 'food1'], as_index=False).sum())
print(grouped.size())
print(grouped.describe())

print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")

# index = pd.date_range('1/1/2014', periods=100)
# ts = pd.Series(np.random.normal(0.5, 2, 100), index)
# print(ts.head())
print("--------------agg分组多种计算----------------")
print(df)
grouped = df.groupby(level='color1')
print(grouped.agg([np.sum, np.mean, np.std]))
print(grouped['a'].agg([np.sum, np.mean, np.std]))
print(grouped['a'].agg({'SUM': np.sum, 'Mean': np.mean}))

print(grouped['a'].agg({'lambda': lambda x: np.mean(abs(x))}))
print(grouped['a'].agg({'C': 'sum', 'D': 'std'}))
print("-------------按月分组-----------")

index = pd.date_range('1/1/2014', periods=100)
ts = pd.Series(np.random.normal(0.5, 2, 100), index)
print(ts.head())
key = lambda x: x.month
print(key)
grouped = ts.groupby(key)
print(grouped.first())












































