N, W = map(int, input().split())
wv = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * (W+1) for _ in range(N+1)]

for i in range(N):
    for j in range(W+1):
        dp[i+1][j] = max(dp[i+1][j], dp[i][j])
        if j+wv[i][0] <= W:
            dp[i+1][j+wv[i][0]] = max(dp[i+1][j+wv[i][0]], dp[i][j] + wv[i][1])

print(max(dp[N]))