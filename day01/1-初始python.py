#乘法口诀表
'''
for i in range(1, 10):
    for j in range(1, i+1):
        print(str(i) + "*" + str(j)+"=" + str(i*j)+"  ", end="")
    print()
'''

#逆向输出乘法口诀表
for i in range(9,0,-1):
    for j in range(1,i+1):
        print(str(i) + "*" + str(j)+"=" + str(i*j)+"\t", end="")
    print()