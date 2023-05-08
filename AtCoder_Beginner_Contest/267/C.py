import numpy as np

N, M = map(int, input().split())

A = list(map(int, input().split()))

pre = [0]
s = 0
for i in range(N):
    s += A[i]
    pre.append(s)

j = 0
ans = []
s = 0
for i in range(M):
    s += A[i] * (i+1)
now = s
ans.append(now)
for i in range(M, N):
    now += - (pre[i] - pre[i-M]) + M * A[i]
    ans.append(now)

print(max(ans))