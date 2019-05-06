import datetime
import time

'''
list1 = [1, 0, 0, 0, 1, 2, 3, 4, 0, 0, 1, 2, 0, 0, 0, 7, 8, 9, 1, 0, 0, 0]
'''

# for i in range(len(list1) - 1):
#     j = i + 1
#     if list1[i] == 0 and list1[j] != 0:
#         count += 1
# if list1[len(list1) - 1] == 0:
#     count += 1
# print(count)
'''
# print(list1.count(0))
import datetime
import time
# t_str1 = '2012-03-05 10:28'
# t_str2 = '2012-03-06 0:52'
t_str3 = '2018/8/4  1:22:02'
t_str4 = '2018/8/5  2:22:02'
# d1 = datetime.datetime.strptime(t_str1, '%Y-%m-%d %H:%M')
# d2 = datetime.datetime.strptime(t_str2, '%Y-%m-%d %H:%M')
# d3 = datetime.datetime.strptime(t_str3, '%Y-%m-%d %H:%M:%S')
part_1, part_2 = t_str3.split("  ")
year, month, day = part_1.split("/")
hour, minute, second = part_2.split(":")
# print(part_1)
# print(part_2)
# print(hour, minute, second)
t_str3 = year + '-' + month + '-' + day + '  ' + hour + ':' + minute + ':' + second
# print(t_str3)
d3 = datetime.datetime.strptime(t_str3, '%Y-%m-%d %H:%M:%S')
print(d3)

part_3, part_4 = t_str4.split("  ")
year1, month1, day1 = part_3.split("/")
hour1, minute1, second1 = part_4.split(":")
# print(part_3)
# print(part_4)
# print(hour, minute, second)
t_str4 = year1 + '-' + month1 + '-' + day1 + '  ' + hour1 + ':' + minute1 + ':' + second1
print(t_str4)
d4 = datetime.datetime.strptime(t_str4, '%Y-%m-%d %H:%M:%S')
# print(d4)
# d = d2 - d1
# print(d)
# d = str(d)

d = d4 - d3
d = str(d)
def t2s(t):
    h, m, s = t.strip().split(":")
    print(h, m, s)
    return int(h) * 3600 + int(m) * 60 + int(s)
print(t2s(d))
'''

# t_str1 = '2012-03-05 10:28:30'
# t_str2 = '2012-03-06 11:52:28'
# d1 = datetime.datetime.strptime(t_str1, '%Y-%m-%d %H:%M:%S')
# d2 = datetime.datetime.strptime(t_str2, '%Y-%m-%d %H:%M:%S')
# print(d1, d2)
# print(type(d1))
# d = d2 - d1
# print(d)
# d = str(d) #1 day, 1 23 58
# print(d)
'''
def transform_time(str):
    part_1, part_2 = str.split("  ")
    year, month, day = part_1.split("/")
    hour, minute, second = part_2.split(":")
    form_time = year + '-' + month + '-' + day + '  ' + hour + ':' + minute + ':' + second
    return form_time

#1 day, 1 23 58
def t2s(d):
    if "day" in d:
        day = d.split("day")[0]
        hour, minute, second = d.split("day")[1].split(",")[1].split(':')
        return int(day) * 86400 + int(hour) * 3600 + int(minute) * 60 + int(second)
    else:
        hour, minute, second = d.split(':')
        return int(hour) * 3600 + int(minute) * 60 + int(second)

t_str1 = '2012/03/05  10:28:30'
t_str2 = '2012/03/06  11:52:28'
t_str1 = transform_time(t_str1)
t_str2 = transform_time(t_str2)
d1 = datetime.datetime.strptime(t_str1, '%Y-%m-%d %H:%M:%S')
d2 = datetime.datetime.strptime(t_str2, '%Y-%m-%d %H:%M:%S')
d = d2 - d1
print(d)
d = str(d)
time_minus = t2s(d)
print(time_minus)
'''
import pandas as pd
import numpy as np
import math
import os

filename = open('F:/Python/泰迪杯数据挖掘竞赛/15193005zo67_C题数据/附件1-示例数据-100辆车/AA00001.csv')
all_data = pd.read_csv(filename)
# all_data
type(all_data)
type(all_data)
#dataFrame转为列表格式处理
gps_speed_data = all_data["gps_speed"]
gps_speed_data = np.array(gps_speed_data)
gps_speed_data = gps_speed_data.tolist()
len(gps_speed_data)
#提取特征1：百公里刹车次数
brake_count = 0
for i in range(len(gps_speed_data) - 1):
    j = i + 1
    if gps_speed_data[i] == 0 and gps_speed_data[j] != 0:
        brake_count += 1
if gps_speed_data[len(gps_speed_data) - 1] == 0:
    brake_count += 1
#brake_count为该车在该段里程中刹车的次数
# brake_count
#获取本车的总里程数
mileage_data = all_data["mileage"]
mileage_data = np.array(mileage_data)
mileage_data = mileage_data.tolist()
mile_all = 0
for i in range(len(mile_data_new)):
    temp_mile = max(mile_data_new[i]) - min(mile_data_new[i])
    mile_all += temp_mile
#mile_all为总里程数
unit_brake_count = math.ceil(brake_count / (mile_all / 100))
#unit_brake_count为百公里刹车次数
unit_brake_count
import datetime
import time
#提取特征3：平均时速
time_data = all_data["location_time"]
time_data = np.array(time_data)
time_data = time_data.tolist()

#存放转化为日期格式的数据
time_time_data = []
#计算时间间隔，转为秒处理
def t2s(d):
    if "day" in d:
        day = d.split("day")[0]
        hour, minute, second = d.split("day")[1].split(",")[1].split(':')
        return int(day) * 86400 + int(hour) * 3600 + int(minute) * 60 + int(second)
    else:
        hour, minute, second = d.strip().split(':')
        return int(hour) * 3600 + int(minute) * 60 + int(second)
for i in range(len(all_data)):
#     time_transform = transform_time(time_data[i])
    time_temp = datetime.datetime.strptime(time_data[i], '%Y-%m-%d %H:%M:%S')
    time_time_data.append(time_temp)
#time_time_data 存放的是将表格中的数据全都变为了时间日期的格式，可加减运算
#存放分段之后的时间数据
time_data_new = []
#存放分段之后的里程数据
mile_data_new = []
k = 0
for i in range(len(all_data) - 1):
    j = i + 1
    #将两个时间相减并转化为字符串格式
    time_minus = str(time_time_data[j] - time_time_data[i])
    if t2s(time_minus) > 7200:
        temp_time_dataList = []
        temp_mile_dataList = []
        for m in range(k, i + 1):
            temp_time_dataList.append(time_time_data[m])
            temp_mile_dataList.append(mileage_data[m])
        time_data_new.append(temp_time_dataList)
        mile_data_new.append(temp_mile_dataList)
        k = j
        i = j
        j = i
    else:
        i += 1
#加上最后一段线路
last_temp_time_dataList = []
last_temp_mile_dataList = []
for i in range(k, len(all_data)):
    last_temp_time_dataList.append(time_time_data[i])
    last_temp_mile_dataList.append(mileage_data[i])
#总的时间段和里程数
time_data_new.append(last_temp_time_dataList)
mile_data_new.append(last_temp_mile_dataList)

print(len(time_data_new))
# print(mile_data_new)
#文件一10段路线
# print(len(mile_data_new))
# mile_all = max(mileage_data) - min(mileage_data)
mile_all = 0
for i in range(len(mile_data_new)):
    temp_mile = max(mile_data_new[i]) - min(mile_data_new[i])
    mile_all += temp_mile
print(mile_all)
sumTime = 0
for i in range(len(time_data_new)):
    print(min(time_data_new[i]))
    print(max(time_data_new[i]))
    time_minus = t2s(str(max(time_data_new[i]) - min(time_data_new[i])))
    sumTime += time_minus
sumTime_hour = float(sumTime) / 3600
print(sumTime_hour)
average_speed = float(mile_all) / sumTime_hour
average_speed

#提取特征四：最高时速/最低时速
gps_speed_data = all_data["gps_speed"]
gps_speed_data = np.array(gps_speed_data)
gps_speed_data = gps_speed_data.tolist()
min_speed = min(gps_speed_data)
print(min_speed)
max_speed = max(gps_speed_data)
print(max_speed)

#提取特征五：平均一次路线连续驾车时长
# time_data_new mile_data_new
routeCount = len(mile_data_new)
sumTime = 0
for i in range(len(time_data_new)):
    time_minus = t2s(str(max(time_data_new[i]) - min(time_data_new[i])))
    sumTime += time_minus
sumTime_hour = float(sumTime) / 3600
everyRouteTime = float(sumTime_hour) / routeCount
everyRouteTime

#提取特征6和7
#先求出任意时刻的加速度
acceleration = [0]
for i in range(1, len(all_data)):
    time_minus = t2s(str((time_time_data[i]) - (time_time_data[i - 1])))
    if time_minus == 0:
        temp_acceleration = acceleration[i - 1]
        acceleration.append(temp_acceleration)
        continue
    speed_minus = int(gps_speed_data[i]) - int(gps_speed_data[i - 1])
    temp_acceleration = float(speed_minus * 1000 / 3600) / time_minus
    acceleration.append(temp_acceleration)
# print(acceleration)
#向文件中加入加速符这一列
# all_data["acceleration"] = acceleration
# all_data.to_csv("F:/Python/泰迪杯数据挖掘竞赛/15193005zo67_C题数据/附件1-示例数据-100辆车/AA00000.csv")

#最大加速度,包括正负
accelerationSum = 0
for i in range(len(acceleration)):
    accelerationSum += acceleration[i]
max_acc = acceleration[0]
for i in range(1, len(acceleration)):
    if max_acc < acceleration[i]:
        max_acc = acceleration[i]
print(max_acc)
min_acc = acceleration[0]
for i in range(1, len(acceleration)):
    if min_acc > acceleration[i]:
        min_acc = acceleration[i]
print(min_acc)

#计算特征：急加速、急减速、急刹车百公里
#查阅资料得当加速度大于3时，且时间持续一秒及以上可判定为急加速，当加速度小于-3时可判定为急减速，小于-4时可判定为急刹车
rapid_acc_count = 0 #急加速计数
rapid_dec_count = 0#急减速计数
rapid_brake_count = 0#急刹车计数
for i in range(len(acceleration)):
    if acceleration[i] > 3:
        rapid_acc_count += 1
    if acceleration[i] < -3:
        rapid_dec_count += 1
    if acceleration[i] < -4:
        rapid_brake_count += 1
eve_rapid_acc_count = math.ceil(float(rapid_acc_count) / (mile_all / 100))
print(eve_rapid_acc_count)
eve_rapid_dec_count = math.ceil(float(rapid_dec_count) / (mile_all / 100))
print(eve_rapid_dec_count)
eve_rapid_brake_count = math.ceil(float(rapid_brake_count) / (mile_all / 100))
print(eve_rapid_brake_count)

#提取特征：转弯时速度>30判定为危险，角度为0.45rad/s，即角速度大于25度判定为转弯

#首先计算角速度
angle_data = all_data["direction_angle"]
angle_data = np.array(angle_data)
angle_data = angle_data.tolist()

angle_rate = [0]
for i in range(1, len(all_data)):
    time_minus = t2s(str((time_time_data[i]) - (time_time_data[i - 1])))
    if time_minus == 0:
        temp_angle_rate= angle_rate[i - 1]
        angle_rate.append(temp_angle_rate)
        continue
    angle_minus = int(angle_data[i]) - int(angle_data[i - 1])
    if angle_minus > 180 or angle_minus <-180:
        angle_minus = 0
    temp_angle_rate = float(angle_minus) / time_minus
    angle_rate.append(temp_angle_rate)
# all_data["angle_rate"] = angle_rate
# all_data.to_csv("F:/Python/泰迪杯数据挖掘竞赛/15193005zo67_C题数据/附件1-示例数据-100辆车/AA00000.csv")
#转弯大于30的次数统计
cornerSpeedCount = 0
for i in range(len(angle_rate)):
    if (angle_rate[i] > 25 or angle_rate[i] < -25) and (gps_speed_data[i] > 30):
        cornerSpeedCount += 1
print(cornerSpeedCount)

#提取特征：百公里怠速时长
acc_state_data = all_data["acc_state"]
acc_state_data = np.array(acc_state_data)
acc_state_data = acc_state_data.tolist()

time_data = all_data["location_time"]
time_data = np.array(time_data)
time_data = time_data.tolist()

gps_speed_data = all_data["gps_speed"]
gps_speed_data = np.array(gps_speed_data)
gps_speed_data = gps_speed_data.tolist()

i = 0
#存放怠速时间总时长
sumDelayTime = 0
#存放怠速时长占引擎工作总时长的比例
sumDelayTime_rate = 0
while (i < len(all_data)):
    if ((gps_speed_data[i] == 0) and (acc_state_data[i] == 1)):
        j = i + 1
        while ((j < len(all_data)) and (gps_speed_data[j] == 0) and (acc_state_data[j] == 1)):
            j += 1
        time_minus = t2s(str((time_time_data[j - 1]) - (time_time_data[i])))
        if time_minus > 600:
#             print(i, j)
#             print(time_minus)
            sumDelayTime += time_minus
        i = j
        j = i + 1
    else:
        i += 1
print(sumDelayTime)
sumDelayTime_rate = float(sumDelayTime) / sumTime
print(sumDelayTime_rate)

#提取特征：熄火滑行的里程数
mileage_data = all_data["mileage"]
mileage_data = np.array(mileage_data)
mileage_data = mileage_data.tolist()

free_Sum = 0
i = 0
while ( i < len(all_data)):
    if acc_state_data[i] == 1:
        i += 1
    else:
        j = i + 1
        while (j < len(all_data) and acc_state_data[j] == 0):
            j += 1
        mile_minus = mileage_data[j - 1] - mileage_data[i]
        print(i, j)
        print(mile_minus)
        free_Sum += mile_minus
        i = j
print(free_Sum)


























































