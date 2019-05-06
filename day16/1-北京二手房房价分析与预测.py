import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', 1000)
pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth', 1000)
from IPython.display import display
plt.style.use("fivethirtyeight")
plt.rc('font', family="SimHei", size=13)
sns.set_style({'font.sana-serif': ['SimHei', 'Arial']})
from sys import version_info
if version_info.major != 3:
    raise Exception('请使用Python3来完成项目')

fname = open('C:/Users/Administrator/Desktop/lianjia.csv')
lianjia_df = pd.read_csv(fname)
# print(lianjia_df)
# display(lianjia_df.head(2))
# print(lianjia_df.info())
# print(lianjia_df.describe())
df = lianjia_df.copy()
# print(df)
df["PerPrice"] = lianjia_df['Price'] / lianjia_df['Size']
#重新摆放列位置
columns = ['Region', 'District', 'Garden', 'Layout', 'Floor', 'Year', 'Size', 'Elevator', 'Direction', 'Renovation', 'PerPrice', 'Price']
df = pd.DataFrame(df, columns=columns)
# print(df.head())

#区域分析
df_house_count = df.groupby('Region')['Price'].count().sort_values(ascending=False).to_frame().reset_index()
# print(df_house_count)
df_house_mean = df.groupby('Region')['PerPrice'].mean().sort_values(ascending=False).to_frame().reset_index()
# print(df_house_mean)
# f, [ax1, ax2, ax3] = plt.subplots(3, 1, figsize=(20, 15))
# sns.barplot(x='Region', y='PerPrice', palette='Blues_d', data=df_house_mean, ax=ax1)
# ax1.set_title("北京各大区二手房每平方单价对比")
# ax1.set_xlabel("区域")
# ax1.set_ylabel("每平米单价")
# sns.barplot(x='Region', y='Price', palette="Greens_d", data=df_house_count, ax=ax2)
# ax2.set_title("北京各大区二手房数量对比")
# ax2.set_xlabel("区域")
# ax2.set_ylabel("数量")
# sns.boxplot(x='Region', y='Price', data=df, ax=ax3)
# ax3.set_title("北京各大区二手房房屋总价", fontsize=15)
# ax3.set_xlabel("区域")
# ax3.set_ylabel("房屋总价")
# plt.show()

#Size特征分析

f, [ax1, ax2] = plt.subplots(1, 2, figsize=(15, 5))
sns.distplot(df['Size'], bins=20, ax=ax1, color='r')
sns.kdeplot(df['Size'], shade=True, ax=ax1)
ax1.set_title("房屋面积的分布情况")
sns.regplot(x='Size', y='Price', data=df, ax=ax2)
ax2.set_title("房屋面积和出售价格的关系")
plt.show()

# print(df.loc[df['Size'] < 10])

#Layout特征分析
# f, ax1 = plt.subplots(figsize=(30, 30))
# sns.countplot(y="Layout", data=df, ax=ax1)
# ax1.set_title("房屋户型", fontsize=15)
# plt.yticks(fontsize=8)
# ax1.set_xlabel("数量")
# ax1.set_ylabel("户型")
# plt.show()

#装修分析
# df_house_renovation = df['Renovation'].value_counts()
#
# # print(df_house_renovation)
#
# f, ax1 = plt.subplots(figsize=(20, 20))
# sns.countplot(y="Renovation", data=df, ax=ax1)
# ax1.set_title("房屋装修情况", fontsize=15)
# plt.yticks(fontsize=8)
# ax1.set_xlabel("数量")
# ax1.set_ylabel("装修情况")
# plt.show()
# # df['Renovation'] = df.loc[(df['Renovation'] != '南北'), 'Renovation']
# f, [ax1, ax2, ax3] = plt.subplots(1, 3, figsize=(20, 5))
# sns.countplot(df['Renovation'], ax=ax1)
# sns.barplot(x='Renovation', y='Price', data=df, ax=ax2)
# sns.boxplot(x='Renovation', y='Price', data=df, ax=ax3)
# plt.show()

##Elevator特征分析
# misn = len(df.loc[(df['Elevator'].isnull()), 'Elevator'])
# print("Elevator缺失值数量为:" + str(misn))
#
# df['Elevator'] = df.loc[(df['Elevator'] == "有电梯") | (df['Elevator'] == "无电梯"), 'Elevator']
# df.loc[(df['Floor'] > 6) & (df['Elevator'].isnull()), 'Elevator'] = "有电梯"
# df.loc[(df['Floor'] <= 6) & (df['Elevator'].isnull()), 'Elevator'] = "无电梯"
# f, [ax1, ax2] = plt.subplots(1, 2, figsize=(20, 10))
# sns.countplot(df['Elevator'], ax=ax1)
# ax1.set_title("有无电梯数量对比", fontsize=15)
# ax1.set_xlabel("是否有电梯")
# ax1.set_ylabel("数量")
# sns.barplot(x="Elevator", y='Price', data=df, ax=ax2)
# ax2.set_title("有无电梯房价对比", fontsize=15)
# ax2.set_xlabel("是否有电梯")
# ax2.set_ylabel("总价")
# plt.show()

# #Year特征分析
# grid = sns.FacetGrid(df, row='Elevator', col="Renovation", palette='seismic', size=4)
# grid.map(plt.scatter, 'Year', 'Price')
# grid.add_legend()
# plt.show()

#Floor分析
# f, ax1 = plt.subplots(figsize=(20, 5))
# sns.countplot(x='Floor', data=df, ax=ax1)
# ax1.set_title("房屋户型", fontsize=15)
# ax1.set_xlabel("数量")
# ax1.set_ylabel("户型")
# plt.show()









































































