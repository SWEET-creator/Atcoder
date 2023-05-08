N, A = map(int, input().split())
x = list(map(int, input().split()))

K = N*N+10
dp = [[[0]*K for j in range(N+1)] for i in range(N+1)]

dp[0][0][0] = 1
for i in range(N):
    for j in range(i+1):
        for k in range(K):
            if dp[i][j][k]:
                dp[i+1][j][k] += dp[i][j][k]
                dp[i+1][j+1][k + x[i]] += dp[i][j][k]

count = 0
for j in range(1, N+1):
        count += dp[N][j][A*j]

print(count)