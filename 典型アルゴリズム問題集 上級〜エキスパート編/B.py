

M, N = map(int, input().split())
S = list(input())
T = list(input())

dp = [[10**18]*(N+1) for _ in range(M+1)]

for i in range(M+1):
    dp[i][0] = i
for j in range(N+1):
    dp[0][j] = j

for i in range(1,M+1):
    for j in range(1,N+1):
        r = 0 if S[i-1] == T[j-1] else 1
        dp[i][j] = min(dp[i][j-1] + 1, dp[i-1][j] + 1, dp[i-1][j-1] + r)

print(dp[M][N])