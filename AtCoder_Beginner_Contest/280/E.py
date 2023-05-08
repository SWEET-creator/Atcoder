N, P = map(int, input().split())

dp = [0 for _ in range(N+1)]

dp[0] = 1
for i in range(N):
    dp[i+1] = dp[i] * (P/100)
    if i+2 <= N:
        dp[i+2] = dp[i] * (1-P/100)

