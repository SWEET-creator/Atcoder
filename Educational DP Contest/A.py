import math

N = int(input())
h = list(map(int, input().split()))

dp = [math.inf for _ in range(N)]

dp[0] = 0
for i in range(N-1):
    if i+1 < N:
        dp[i+1] = min(dp[i+1], dp[i] + abs(h[i+1]- h[i]))
    if i+2 < N:
        dp[i+2] = min(dp[i+2], dp[i] + abs(h[i+2]- h[i]))

print(dp[-1])