N, S = map(int, input().split())
dp = [[False]*(S+1) for i in range(N+1)]
data = []

dp[0][0] = 1
for i in range(1, N+1):
    a, b = map(int, input().split())
    for j in range(S+1):
        if dp[i-1][j]:
            if j + a <= S:
                dp[i][j+a] = True
            if j + b <= S:
                dp[i][j+b] = True
    data.append([a,b])

data = data[::-1]
if dp[N][S]:
    print("Yes")
    o = S
    out = []
    for i in range(N):
        if dp[N-(i+1)][o - data[i][0]] == True:
            o -= data[i][0]
            out.append("H")
        else:
            o -= data[i][1]
            out.append("T")
    out = out[::-1]
    print("".join(out))
else:
    print("No")
