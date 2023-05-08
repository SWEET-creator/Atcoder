import numpy as np

N = int(input())
S = list(input())
W = list(map(int, input().split()))

data = [0]*N
for i in range(N):
    data[i] = [int(W[i]),int(S[i])]

col_num = 0
data = sorted(data, key = lambda x:x[0])

t_list = []
t_0 = 0
for i in range(N):
    if data[i][1] == 0:
        t_0 += 1
    t_list.append(t_0)

t_1 = 0
for i in range(N):
    if data[N-i-1][1] == 1:
        t_1 += 1
    t_list[N-i-1] += t_1

print(max(t_list))
        