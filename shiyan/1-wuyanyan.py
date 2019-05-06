import pandas as pd
import numpy as np

edge_filename = open(r'C:/Users/Administrator/Desktop/吴艳艳/edge.csv')
edge_data = pd.read_csv(edge_filename)


CRNAE_filename = open(r'C:/Users/Administrator/Desktop/吴艳艳/lncRNA_miRNA.csv')
CRNAE_data = pd.read_csv(CRNAE_filename)
cRNAE = CRNAE_data["lncRNA"]
cRNAE = list(set(cRNAE))

MRNAE_filename = open(r'C:/Users/Administrator/Desktop/吴艳艳/lncRNA_miRNA2.csv')
MRNAE_data = pd.read_csv(MRNAE_filename)
mRNAE = MRNAE_data["lncRNA"]
mRNAE = list(set(cRNAE))

num = 0
e_num = []
for i in range(0, len(edge_data)):
    if edge_data.iloc[i]["fromNode"] in cRNAE and edge_data.iloc[i]["toNode"] in cRNAE:
        num += 1
        e_num.append(i)
    elif edge_data.iloc[i]["fromNode"] in mRNAE and edge_data.iloc[i]["toNode"] in mRNAE:
        num += 1
        e_num.append(i)
print(num)
print(e_num)

d = pd.DataFrame(columns=['fromNode', 'toNode', 'weight', 'direction', 'fromAltName', 'toAltName'])
# print(d)
# print(type(d))
# d = d.append([{'fromNode': edge_data.iloc[0:1]["fromNode"]}], ignore_index=True)
# print(d)

# row = {'fromNode': 1, 'toNode': "123", 'weight': 123, 'direction': 1, 'fromAltName': 1, 'toAltName': 1}
# d = d.append(row, ignore_index=True)
# print(d)
# d.to_csv(r'C:/Users/Administrator/Desktop/1.csv')

for i in e_num:
    fromNode = edge_data.iloc[i:i + 1]["fromNode"].values[0]
    toNode = edge_data.iloc[i:i + 1]["toNode"].values[0]
    weight = edge_data.iloc[i:i + 1]["weight"].values[0]
    direction = edge_data.iloc[i:i + 1]["direction"].values[0]
    fromAltName = edge_data.iloc[i:i + 1]["fromAltName"].values[0]
    toAltName = edge_data.iloc[i:i + 1]["toAltName"].values[0]
    # print(fromNode, toNode, weight, direction, fromAltName, toAltName)
    row = {'fromNode': fromNode, 'toNode': toNode, 'weight': weight,
           'direction': direction, 'fromAltName': fromAltName, 'toAltName': toAltName}
    d = d.append(row, ignore_index=True)
print(d)
d.to_csv(r'C:/Users/Administrator/Desktop/1.csv')








































