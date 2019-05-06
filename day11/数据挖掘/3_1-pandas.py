import pandas as pd
import numpy as np

dates = pd.date_range("20140729", periods=6)
print(dates)
print(type(dates))
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))
print(df)
df2 = pd.DataFrame({"A": np.random.randn(6)})
print(df2)

df2 = pd.DataFrame({"A": pd.Timestamp("20140729"), "B": pd.Series(1)}, index=("one",))
print(df2)

df2 = pd.DataFrame({"A": pd.Timestamp("20140729"), "B": pd.Series(1, index=list(range(4)))})
print(df2)
print(type(df2))
print(df2.dtypes)

print(df.head())
print(df.head(2))
print(df.tail())

print(df.index)
print(df.columns)

print(df)
print(df.values)
print(type(df.values))
print(df.values[0][1])

print(df.describe())
print(type(df.describe()))

print(df.T)
print(df)
print(df.sort_values(by="C"))

print("-----------------------------------")
print(df)
print(df['A'])
print(df[1:3])
print(df["20140729": "20140730"])
print(df.loc["20140729":"20140730", ['A', 'B']])
print(df.loc[dates[0], 'A'])

print("------------------------------------")
print(df)
print(df.iloc[3:4])
print(df.iloc[3])
print(type(df.iloc[3]))
print(df.iloc[[1, 2, 4], [0, 2]])
print(df.iloc[1:3, :])
print(df.iloc[1, 1])
print(df.iat[1, 1])

print("--------------------------------------")
print(df)
print(df[df.D > 0])
print(df[(df.D > 0) & (df.C > 0)])
print(df[['A', 'B']][(df.D > 0) & (df.C > 0)])
index = (df.D > 0) & (df.C > 0)
print(index)
print(df[index])

alist = [0.325557, 0.004100, 1.325165]
print(df['D'].isin(alist))
print("----------------------------------------")















































































































