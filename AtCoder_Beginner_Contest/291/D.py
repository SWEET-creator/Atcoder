N = int(input())

M = 998244353

dp = [[0,0] for i in range(N)]
data = [[0,0] for i in range(N)]

for i in range(N):
    data[i][0], data[i][1] = map(int, input().split())
    if i == 0:
        dp[i] = [1, 1]
    else:
        for pre in range(2):
            for nxt in range(2):
                if data[i][pre] != data[i-1][nxt]:
                    dp[i][nxt] += dp[i-1][pre]
    
    dp[i][0] = dp[i][0]%M
    dp[i][1] = dp[i][1]%M

print((dp[N-1][0] + dp[N-1][1])%M)