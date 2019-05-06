print("--------------删除缺失数据-------------------")
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(5, 3), index=list("abcde"), columns=['one', 'two', 'three'])
df.ix[1, :] = np.nan
df.ix[1:-1, 2] = np.nan
print(df)
print(df.dropna(axis=0))
print(df)
print(df.dropna(axis=1))
print("-------------插值法填补缺失值---------------")
print(df.interpolate())
df.index = [1, 2, 3, 4, 5]
print(df.interpolate(method='values'))

print("----------------值替换---------------")
ser = pd.Series([0, 1, 2, 3, 4, 5, 1, 2, 3])
print(ser)
print(ser.replace(0, 6))
print(ser.replace([0, 1, 2, 3, 4, 5], [5, 4, 3, 2, 1, 0]))
print(ser.replace({1: 11, 2: 22}))
df = pd.DataFrame({'a': [0, 11, 22, 3, 4, 2], "b": [5, 62, 2, 2, 8, 9]})
print(df)
print(df.replace(2, 20))
print(df['a'].replace([0, 1, 2, 3, 4, 5], [5, 4, 3, 2, 1, 0]))
print(df[['a', 'b']].replace(2, 10))
print(df)
print(df.replace({'a': 0, 'b': 5}, np.nan))
print(df['a'].replace([1, 2, 3], method='pad'))











































































