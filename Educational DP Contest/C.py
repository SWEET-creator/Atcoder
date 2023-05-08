N = int(input())

data = []
for i in range(N):
    data.append(list(map(int, input().split())))

K = 3
dp = [[0] * K for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(K):
            dp[i][j] = max(data[i-1][j]+dp[i-1][(j-1)%K], dp[i][j])
            dp[i][j] = max(data[i-1][j]+dp[i-1][(j+1)%K], dp[i][j])

print(max(dp[N]))