import numpy as np
s = list(input())
t = list(input())

dp = [[[] for _ in range(len(t))] for _ in range(len(s))]

for i in range(len(s)):
    for j in range(len(t)):
        dp[i][j] = dp[i-1][j]
        if s[i] == t[j]:
            dp[i][j].append(dp[i][j-1].append(t[j]))
        else:
            dp[i][j] = dp[i][j-1]

print(dp)