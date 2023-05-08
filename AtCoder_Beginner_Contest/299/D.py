import numpy as np

N = int(input())

a = 1
b = N
data = []
flag = False

for i in range(20):
    mid = (a+b)//2
    print("?", mid)
    s = int(input())
    if s == 0:
        a = mid + 1
    else:
        b = mid - 1
    data.append([mid,s])
    data  = np.sort(data, axis = 0)
    data = list(data)
    for j in range(len(data)-1):
        if data[j][0]+1 == data[j+1][0]:
            if data[j][1] != data[j+1][1]:
                print("!", data[j][0])
                flag = True
                break
    if flag:
        break