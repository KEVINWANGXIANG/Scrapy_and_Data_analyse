import pandas as pd
import numpy as np
pd.set_option('display.max_columns', 1000)
pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth', 1000)

fname = open(r'C:/Users/Administrator/Desktop/lianjia2.csv')
lianjia_df = pd.read_csv(fname)
# print(lianjia_df)
# lianjia_df['Elevator'] = lianjia_df.loc[(lianjia_df['Elevator'] == "有电梯") | (lianjia_df['Elevator'] == "无电梯"), 'Elevator']
# lianjia_df.loc[(lianjia_df['Floor'] > 6) & (lianjia_df['Elevator'].isnull()), 'Elevator'] = "有电梯"
# lianjia_df.loc[(lianjia_df['Floor'] <= 6) & (lianjia_df['Elevator'].isnull()), 'Elevator'] = "无电梯"
# # print(lianjia_df)
# # print(type(lianjia_df))
# lianjia_df.to_csv(r'C:/Users/Administrator/Desktop/lianjia2.csv', encoding="utf_8_sig")
# lianjia_df.loc[(lianjia_df['Renovation'] == '南北'), 'Renovation'] = "其他"
# print(lianjia_df)
# df_house_renovation = lianjia_df['Renovation'].value_counts()
# lianjia_df.to_csv(r'C:/Users/Administrator/Desktop/lianjia2.csv', encoding="utf_8_sig")
# print(df_house_renovation)
#删除含有空格的一整行
# lianjia_df = lianjia_df.dropna()
# print(lianjia_df)









































