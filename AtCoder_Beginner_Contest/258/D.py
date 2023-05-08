import numpy as np
N, X = map(int ,input().split())

A = []
B = []
for i in range(N):
    a, b  = map(int, input().split())
    A.append(a)
    B.append(b)

pre = []
s = 0
for i in range(N):
    s += A[i] + B[i]
    pre.append(s)

c = X
exp = []
for i in range(N):
    c -= 1
    if c == 0:
        break
    exp.append(c * B[i])

ans = np.inf
for i in range(min(len(pre), len(exp))):
    if ans > pre[i] + exp[i]:
        ans = pre[i] + exp[i]
print(ans)