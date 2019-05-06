print("-----------散点图和抖动图-----------")
import pandas as pd
import numpy as np
from statsmodels.formula.api import ols
import matplotlib.pylab as pyl
'''
fname = open('C:/Users/Administrator/Desktop/lianjia.csv')
df = pd.read_csv(fname)
# print(df.head())
x = df['Size']
# print(x)
y = df["Price"]
# print(y)
plt = df.plot(kind="scatter", x='Size', y='Price').get_figure()
# plt.savefig('C:/Users/Administrator/Desktop/price.png')

def jitter(seris, factor):
    z = float(seris.max()) - float(seris.min())
    a = float(factor) * z / 50
    return seris.apply(lambda x: x + np.random.uniform(-a, a))

df2 = df
df["Size"] = jitter(df["Size"], 1)
df["Price"] = jitter(df["Price"], 1)
print(df["Size"])
plt = df2.plot(kind="scatter", x='Size', y='Price', alpha=.5).get_figure()
# plt.savefig('C:/Users/Administrator/Desktop/price.png')

print("-----------散点图添加趋势线---------------")

lm = ols("Size~Price", df).fit()
pyl.plot(df['Size'], df['Price'], 'ob')
pyl.plot(df['Price'], lm.fittedvalues, 'r', linewidth=2)
# pyl.show()

print("------------柱形图------------")
df = pd.DataFrame(np.random.rand(10, 4), columns=list("abcd"))
# pd.set_option('mpl_style', 'default')
print(df.head())
# plt = df.plot(kind="bar", stacked=True).get_figure()
plt = df.plot(kind="barh", stacked=True).get_figure()
# plt.savefig('C:/Users/Administrator/Desktop/plot.png')
'''
print("-----------------------直方图------------------------")
df = pd.DataFrame(np.random.rand(100, 4), columns=list("abcd"))
print(df.head())
df['a'].hist().get_figure().savefig('C:/Users/Administrator/Desktop/plot1.png')
print("------------------------箱型图------------------------")
fig, ax = pyl.subplots()
print(fig)
print(ax)
df = pd.DataFrame(np.random.rand(100, 2), columns=list("ab"))
df.boxplot(ax=ax)
# pyl.savefig('C:/Users/Administrator/Desktop/plot2.png')
import pandas.util.testing as tm
df['x'] = tm.np.random.choice(['F', 'M'], size=100)
df.boxplot(ax=ax, by='x')
pyl.savefig('C:/Users/Administrator/Desktop/plot3.png')




































