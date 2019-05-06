
import numpy as np

a = [[1, 2, 3, 4], [5, 6, 7, 8]]
b = np.array(a)
print(b)
print(type(b))
print(len(a))

#查看属性
print(b.size)
#数组形状
print(b.shape)
#数组维度
print(b.ndim)
#数组元素类型
print(b.dtype)

#创建10行10列的数值为浮点1的矩阵
array_one = np.ones([10, 10])
print(array_one)
#创建10行8列的数值为浮点0的矩阵
array_zero = np.zeros([10, 8])
print(array_zero)

#均匀分布
#创建指定形状（示例是10行10列）的数组（0到1之间）
arr1 = np.random.rand(10, 10)
print(arr1)
#创建指定范围内的一个数
num1 = np.random.uniform(0, 100)
print(num1)
#创建指定范围内的一个整数
num2 = np.random.randint(0, 100)
print(num2)

#正态分布
arr2 = np.random.normal(1.75, 0.1, (4, 5))
print(arr2)
print(arr2[1:3, 2:4])

one_20 = np.ones([20])
print(one_20)

one_4_5 = one_20.reshape([4, 5])
print(one_4_5)

#Numpy计算
stus_score = np.array([[80, 88], [82, 81], [84, 75], [86, 83], [75, 81]])
print(stus_score > 80)
#小于80替换为0，大于等于80替换为90
print(np.where(stus_score < 80, 0, 90))

print("每一列的最大值是:")
result = np.amax(stus_score, axis=0)
print(result)

print("每一行的最大值：")
result1 = np.amax(stus_score, axis=1)
print(result1)

print("每一行最小值：")
result2 = np.amin(stus_score, axis=1)
print(result2)
print("每一列的最小值:")
result3 = np.amin(stus_score, axis=0)
print(result3)

print("每一行平均值：")
result4 = np.mean(stus_score, axis=1)
print(result4)
print("每一列的平均值:")
result5 = np.mean(stus_score, axis=0)
print(result5)

print("每一行方差：")
result6 = np.std(stus_score, axis=1)
print(result6)
print("每一列的方差:")
result7 = np.std(stus_score, axis=0)
print(result7)

#数组与数的运算
# stus_score[:, 0:1] = stus_score[:, 0:1] + 5
# print(stus_score)

q = np.array([[0.4], [0.6]])
result = np.dot(stus_score, q)
print(result)

#矩阵拼接
v1 = [[0, 1, 2, 3, 4, 5],
      [6, 7, 8, 9, 10, 11]]
v2 = [[12, 13, 14, 15, 16, 17],
      [18, 19, 20, 21, 22, 23]]
result = np.vstack((v1, v2))
print(result)

result = np.hstack((v1, v2))
print(result)

v3 = [1, 2, 3]
v4 = [4, 5, 6]
result = zip(v3, v4)
result = list(result)
print(result)

arr3 = np.arange(15).reshape(3, 5)
print(arr3)
print(type(arr3))

result3 = np.sum(stus_score, axis=0)
print(result3)

#迭代
for item in stus_score.flat:
    print(item)

#
# print(stus_score.ravel())
# print(type(stus_score.ravel()))
# print(stus_score.ravel()[2])

print(np.vsplit(stus_score, 5))

print(np.hsplit(stus_score, 2))









































