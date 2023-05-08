import numpy as np

N = 10
binom = [[0]*N for i in range(N)]

for i in range(N):
    binom[i][0] = 1
    for j in range(1, i):
        binom[i][j] = binom[i-1][j-1] + binom[i-1][j]

print(np.array(binom))