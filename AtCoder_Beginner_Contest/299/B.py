import numpy as np
N, T = map(int, input().split())
C = list(map(int, input().split()))
R = list(map(int, input().split()))

e = []
index = []

ee = []
eindex = []
for i in range(N):
    if T == C[i]:
        e.append(R[i])
        index.append(i)
    if C[0] == C[i]:
        ee.append(R[i])
        eindex.append(i)

if len(e):
    arg = np.argmax(e)
    print(index[arg]+1)
else:
    arg = np.argmax(ee)
    print(eindex[arg]+1)