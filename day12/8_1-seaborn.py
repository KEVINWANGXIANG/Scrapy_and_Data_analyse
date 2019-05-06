import matplotlib.pylab as plt
import seaborn as sns
import numpy as np
import pandas as pd

sns.set_style("white")

'''
sns.set(style="white", palette="muted", color_codes=True)
plt.plot(np.arange(10), np.arange(10))
plt.show()
'''
'''
#displot()是hist加强版， kdeplot()为密度曲线图
df_iris = pd.read_csv(r'C:/Users/Administrator/Desktop/iris.csv')
fig, axes = plt.subplots(1, 2)
# x = [1, 2, 3, 4, 5]
# sns.distplot(x, ax=axes[0], kde=True, rug=True)
sns.distplot(df_iris['Petal.Length'], ax=axes[0], kde=True, rug=True)
sns.kdeplot(df_iris['Petal.Length'], ax=axes[1], shade=True)
plt.show()
'''

'''
rs = np.random.RandomState(100)
d = rs.normal(size=10)
print(d)
f, axes = plt.subplots(2, 2, figsize=(7, 7), sharex=True)
sns.distplot(d, kde=False, color='b', ax=axes[0, 0])
sns.distplot(d, hist=False, rug=True, color='r', ax=axes[0, 1])
sns.distplot(d, hist=False, rug=False, color="g", kde_kws={"shade":True}, ax=axes[1, 0])
sns.distplot(d, color="m", ax=axes[1, 1])
plt.show()
'''

'''
print("------------------箱线图、小提琴图----------------")
df_iris = pd.read_csv(r'C:/Users/Administrator/Desktop/iris.csv')
# print(df_iris)
# print(type(df_iris))
# print(df_iris['Class'])
# sns.boxplot(x=df_iris['Class'], y=df_iris['Sepal.Width'], hue_order=["setosa", "versicolor", "virginica"], fliersize=1)
sns.violinplot(x=df_iris['Class'], y=df_iris['Sepal.Width'], hue_order=["setosa", "versicolor", "virginica"], fliersize=1)
plt.show()
'''

'''
print("---------------------联合分布jointplot()--------------------")
df_iris = pd.read_csv(r'C:/Users/Administrator/Desktop/iris.csv')
# sns.jointplot(x=df_iris['Petal.Length'], y=df_iris['Petal.Width'])
sns.jointplot(x=df_iris['Petal.Length'], y=df_iris['Petal.Width'], kind="reg")
plt.show()
'''
'''
print("-----------------热点图-------------------")
uniform_data = np.random.rand(10, 12)
print(uniform_data)
ax = sns.heatmap(uniform_data, vmin=0, vmax=1)
plt.show()
'''
'''
print("------------------散点图------------------")
df_iris = pd.read_csv(r'C:/Users/Administrator/Desktop/iris.csv')
f, ax = plt.subplots(figsize=(10, 7))
plt.scatter(x=df_iris['Petal.Length'], y=df_iris['Petal.Width'], c='r')
plt.show()
'''
'''
print("------------------pointplot------------------")
df_iris = pd.read_csv(r'C:/Users/Administrator/Desktop/iris.csv')
f, ax = plt.subplots(figsize=(10, 7))
sns.pointplot(x=df_iris['Petal.Length'], y=df_iris['Petal.Width'], c='r')
plt.xticks(rotation='horizontal')
plt.show()
'''
'''
print("------------------------pairplot-------------------")
df_iris = pd.read_csv(r'C:/Users/Administrator/Desktop/iris.csv')
sns.pairplot(df_iris, vars=['Petal.Length', 'Petal.Width', 'Sepal.Length', 'Sepal.Width'], hue="Class",palette="husl")
plt.show()
'''
# df_iris = pd.read_csv(r'C:/Users/Administrator/Desktop/iris.csv')
# grid = sns.FacetGrid(df_iris, row='Petal.Length', col='Petal.Width', palette='seismic', size=4)
# plt.show()

'''
print("-----------------barplot()---------------------")
df_iris = pd.read_csv(r'C:/Users/Administrator/Desktop/iris.csv')
sns.barplot(x=df_iris["Petal.Width"], y=df_iris["Petal.Length"], orient='v', alpha=0.8, color='red')
plt.xlabel('Petal.Width', fontsize=16)
plt.ylabel('Petal.Length', fontsize=16)
plt.yticks(fontsize=15)
plt.show()
'''

'''
print("------------------bar图-------------------------")
plt.rc('font', family="SimHei", size=13)
num = np.array([13325, 9403, 9227, 8651])
ratio = np.array([0.75, 0.76, 0.72, 0.75])
men = num * ratio
women = num * (1-ratio)
x = ["聊天", "支付", "团购\n优惠券", "在线视频"]
width = 0.5
idx = np.arange(len(x))
plt.bar(x, men, width, color="red", label="男性用户")
plt.bar(x, women, width, bottom=men, color="yellow", label="女性用户")
plt.xlabel("应用类别")
plt.ylabel("男女分布")
plt.xticks(x, rotation=40)

for a, b in zip(idx, men):
    plt.text(a, b + 0.05, '%.0f'%b, ha="center", va="bottom", fontsize=12)
for a, b, c in zip(idx, women, men):
    plt.text(a, b  + c +0.5, '%.0f'%b, ha='center', va="bottom", fontsize=12)
plt.legend()
plt.show()

'''
'''
print("-------------------双Y轴绘图---------------------------")
fname = open("C:/Users/Administrator/Desktop/b.csv")
df = pd.read_csv(fname, index_col='chn_name')
df.index.name = "国家"
plt.rc('font', family="SimHei", size=13)
plt.figure()
df["GDP"].plot(kind='bar')
plt.ylabel('GDP')
plt.title("国家发展情况对比")

p = df["rate"]
p.plot(color='black', secondary_y=True, style='--o', linewidth=2)
plt.ylabel("增长速度")
x = [0, 1, 2, 3, 4]
for a, b in zip(x, p):
    plt.text(a+0.1, b+0.02, '%.2f'%b, ha='center', va="bottom", fontsize=12)
plt.show()
'''

print("-----------------饼状图---------------------")
import matplotlib.mlab as mlab

fname = open('C:/Users/Administrator/Desktop/lianjia.csv')
df = pd.read_csv(fname)
df = df.head(50)
df_direction = df["Direction"]
# print(df_direction)

direction = df_direction.value_counts()
de_ph = pd.DataFrame({'dir': direction.index[1:], 'fre': direction.values[1:]})
# print(direction)
plt.rc("font", family='SimHei', size=13)
fig = plt.figure()
plt.pie(de_ph.fre,labels=de_ph.dir, autopct='%1.2f%%')
plt.title("租房方位")
plt.show()





















































































