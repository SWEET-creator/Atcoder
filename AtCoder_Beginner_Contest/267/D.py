import numpy as np

N, M = map(int, input().split())

A = list(map(int, input().split()))

dp = [[-np.inf]*(M+1) for i in range(N)]

dp[0][0] = 0
dp[0][1] = A[0]
for i in range(1, N):
    for j in range(min(M+1, i+2)):
        if j == 0:
            dp[i][j] = 0
        else:
            dp[i][j] = max(dp[i-1][j-1] + A[i]*j, dp[i-1][j])
print(dp)