N = int(input())
T_max = 10**5
X = [0]*(T_max+1)
A = [0]*(T_max+1)


for i in range(N):
    t, x, a = map(int, input().split())
    X[t] = x
    A[t] = a
dp = [[-10**18]*(5) for _ in range(T_max+1)]

dp[0][0] = 0
for i in range(1,T_max+1):
    for j in range(5):
        if 0 < j and j < 4:
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j], dp[i-1][j+1])
        elif j == 0:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j+1])
        elif j == 4:
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j])
    dp[i][X[i]] += A[i]

print(max(dp[T_max]))