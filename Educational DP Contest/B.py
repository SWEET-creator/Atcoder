N, K = map(int, input().split())
h = list(map(int, input().split()))
dp = [float("inf") for _ in range(N)]
dp[0] = 0

for i in range(1,N):
    dp[i]= min([float("inf")]+[dp[i-j] + abs(h[i] - h[i-j]) for j in range(1,K+1) if i - j >= 0])
print(dp[-1])