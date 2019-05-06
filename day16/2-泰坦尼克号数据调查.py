import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from decimal import Decimal
import seaborn as sns
from fractions import Fraction
import scipy
pd.set_option('display.max_columns', 1000)
pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth', 1000)
plt.style.use("fivethirtyeight")
plt.rc('font', family="SimHei", size=13)
sns.set_style({'font.sana-serif': ['SimHei', 'Arial']})

fname = open(r'F:/Python/数据分析练习/泰坦尼克数据分析/Data_Exploration-master/Data_Exploration-master/titanic_data/titanic-data.csv')
titanic_df = pd.read_csv(fname)
# print(titanic_df)
# print(titanic_df.head())
# print(titanic_df.describe())
#设计一个函数，返回一个字典，字典的key是字段名，value是该字段有Nan值的个数
def get_null_record(df):
    dict_null = {}
    for column in df.columns:
        if not len(df[df[column].isnull()]) == 0:
            dict_null[column] = len(df[df[column].isnull()])
    return dict_null
data_null_dict = get_null_record(titanic_df)
# print(data_null_dict)
# print(len(titanic_df))
#inplace=True,不创建新的对象,直接在原始对象上进行修改;
titanic_df['Cabin'].fillna('Unknown', inplace=True)
mean_age = titanic_df['Age'].mean()
titanic_df['Age'].fillna(mean_age, inplace=True)
titanic_df['Embarked'].fillna('S', inplace=True)
# print(titanic_df)
# print(get_null_record(titanic_df))


#Q1：年龄与乘客生还的情况怎么样
#单变量探索：生还或生还数
# df_survived_data = titanic_df['Survived'].value_counts()
# # print(df_survived_data)
# f, ax1 = plt.subplots(figsize=(10, 10))
# sns.countplot(x='Survived', data=titanic_df, ax=ax1)
# plt.yticks(fontsize=15)
# ax1.set_xlabel("生还/未生还")
# ax1.set_ylabel("人数")
# plt.show()

#单变量探索：年龄
# df_age_data = titanic_df['Age'].value_counts()
# # print(df_age_data)
# f, ax1 = plt.subplots(figsize=(10, 10))
# sns.countplot(x='Age', data=titanic_df, ax=ax1)
# plt.yticks(fontsize=15)
# plt.xticks(fontsize=6)
# ax1.set_xlabel("年龄分布")
# ax1.set_ylabel("人数")
# plt.show()
# plt.hist(titanic_df['Age'])
# plt.show()

#计算年龄段与生还的相关系数
age_max = titanic_df["Age"].max()
print(age_max)
age_min = titanic_df['Age'].min()
print(age_min)
bins = np.arange(0, 90, 12)
# print(bins)
#黑科技,haha，新增一个变量Age_group,对应每个Age变量所输年龄的标签
titanic_df["Age_group"] = pd.cut(titanic_df['Age'], bins)
# print(titanic_df.head())
r = titanic_df['Survived'].corr(titanic_df['Age_group'], method='kendall')
# print(r)

#计算各年龄段和乘客生还的数据
df_total_count_each_age_group = titanic_df.groupby(['Age_group'], as_index=False)["PassengerId"].count()
# print(df_total_count_each_age_group)
df_survival_count_each_age_group = titanic_df[titanic_df['Survived'] == 1].groupby(['Age_group'], as_index=False)["PassengerId"].count()
print(df_survival_count_each_age_group)

#计算每个年龄段的生还率
survival_rate_each_group = df_survival_count_each_age_group["PassengerId"] / df_total_count_each_age_group["PassengerId"]
survival_rate_each_group = pd.Series(survival_rate_each_group.values, index=df_total_count_each_age_group["Age_group"])
# print(survival_rate_each_group)

#可视化年龄段和生还率
# print(df_total_count_each_age_group)
# titanic_df.groupby(['Age_group'])['PassengerId'].count().plot(kind='bar')
# plt.title("Count vs Age_group")
# plt.xticks(fontsize=8)
# plt.ylabel("count")
# plt.show()
# titanic_sur_df = titanic_df[titanic_df['Survived'] == 1]
# # print(titanic_sur_df)
# titanic_sur_df.groupby(['Age_group'])["PassengerId"].count().plot(kind='bar')
# plt.show()
#可视化每个年龄段的生还率
# survival_rate_each_group.plot(kind="bar")
# plt.show()



#Q2:性别与乘客生化的情况
#单变量探索:性别
sex_data = titanic_df.groupby(["Sex"])['PassengerId'].count()
# sex_data.plot(kind="bar")
# plt.title("Count vs Sex")
# plt.xlabel("Sex")
# plt.ylabel("Count")
# plt.show()

#计算性别与生还的相关系数
r = titanic_df['Survived'].corr(titanic_df['Sex'], method='kendall')
# print(r)
#计算性别与生还的数据
total_count_sex = titanic_df.groupby(["Sex"])["PassengerId"].count()
# print(total_count_sex)
survival_count_sex = titanic_df[titanic_df['Survived'] == 1].groupby(["Sex"])["PassengerId"].count()
# print(survival_count_sex)
survival_rate_sex = survival_count_sex / total_count_sex
# print(survival_rate_sex)

# ax1 = plt.subplot(1, 2, 1)
# survival_count_sex.plot(kind="bar", color="Blue")
# ax1.set_ylabel("Survival Count")
# ax2 = plt.subplot(1, 2, 2)
# survival_rate_sex.plot(kind="bar", color="Purple")
# ax2.set_ylabel("Survival Rate")
# plt.show()

#不同的票等级与乘客的生还情况
#单变量探索，船上三个票登记的乘客的分布情况
count_each_pclass = pd.Series(titanic_df.groupby(["Pclass"])["PassengerId"].count().values,
                              index=['1-Upper', '2-Middle', '3-Lower'])
# count_each_pclass.plot(kind="pie", autopct="%1.1f%%", shadow=True, explode=[0.05, 0.05, 0.05])
#保证饼状图是正圆,否则会有一点角度偏斜
# plt.axis('equal')
# plt.ylabel(" ")
# plt.show()
r = titanic_df["Pclass"].corr(titanic_df["Survived"], method='kendall')
# print(r)
survived_count_each_class = pd.Series(titanic_df[titanic_df["Survived"] == 1].groupby("Pclass")["PassengerId"].count().values,
                                      index=['1-Upper', '2-Middle', '3-Lower'])
# print(survived_count_each_class)
survived_rate_each_pclass = survived_count_each_class / count_each_pclass
# print(survived_rate_each_pclass)
#可视化票等级与生还率
# ax1 = plt.subplot(121)
# survived_count_each_class.plot(kind="bar", color="Green")
# ax1.set_ylabel("Survival Count")
# ax1.set_title("Survival Vs Count")
#
#
# ax2 = plt.subplot(122)
# survived_rate_each_pclass.plot(kind="bar", color="Red")
# ax2.set_ylabel("Survival Rate")
# ax2.set_title("Survival vs Rate")
#
# plt.show()

#Q4:不同登录港口的乘客与生还情况
count_from_each_port = titanic_df.groupby(["Embarked"])["PassengerId"].count()
# print(count_from_each_port)
# survived_count_from_port = pd.Series(titanic_df[titanic_df["Survived"] == 1].groupby("Embarked")["PassengerId"].count(),
#                                      index=["C", "Q", "S"])
# survived_count_from_port.plot(kind="pie", autopct="%1.1f%%", shadow=True, explode=[0.05, 0.05, 0.05])
# plt.show()

r = titanic_df["Survived"].corr(titanic_df["Embarked"], method="kendall")
print(r)

survived_count_each_port = titanic_df[titanic_df["Survived"] == 1].groupby("Embarked")["PassengerId"].count()
# print(survived_count_each_port)

survived_rate_each_port = survived_count_each_port / count_from_each_port
# print(survived_rate_each_port)

#可视化每个港口的生还率
# ax1 = plt.subplot(121)
# survived_count_each_port.plot(kind="bar", color="Green")
# ax1.set_ylabel("Survival Count")
# ax1.set_title("Survival Vs Port")
#
#
# ax2 = plt.subplot(122)
# survived_rate_each_port.plot(kind="bar", color="Red")
# ax2.set_ylabel("Survival Rate")
# ax2.set_title("Survival vs Port")
# # plt.subplots_adjust(left=0.2, right=2, wspace=0.4)
# plt.show()


#Q5:费用与票价等级的关系
# titanic_df["Fare"].hist()
# plt.title("Hist plot of Fare")
# plt.show()

#费用等级与费用的箱线图
# sns.boxplot(x='Pclass', y='Fare', data=titanic_df, hue_order=["1-Upper", "2-Middle", "3-Lower"], fliersize=1)
# plt.show()

r = titanic_df["Fare"].corr(titanic_df["Pclass"], method="kendall")
print(r)

#Q6:不同费用的乘客的生还情况如何？
fare_survival = titanic_df[titanic_df["Survived"] == 1]['Fare']
fare_unsurvival = titanic_df[titanic_df["Survived"] == 0]['Fare']
# plt.boxplot([fare_survival, fare_unsurvival], labels=["Survived", "Not Survived"])
# plt.ylim([-20, 550])
# plt.ylabel('Fare', fontsize=20)
# plt.show()

#Q7:从三个港口登录的乘客费用是否有所不同
fare_c = titanic_df[titanic_df["Embarked"] == "C"]['Fare']
fare_q = titanic_df[titanic_df["Embarked"] == "Q"]['Fare']
fare_s = titanic_df[titanic_df["Embarked"] == "S"]['Fare']
plt.boxplot([fare_c, fare_q, fare_s], labels=["C", "Q", "S"])
plt.show()



















































































































































