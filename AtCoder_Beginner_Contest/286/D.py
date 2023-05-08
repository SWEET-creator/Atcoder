N, X = map(int, input().split())

l = []

dp = [False for i in range(X+1)]

dp[0] = True
flag = False
for _ in range(N):
    a, b = map(int, input().split())
    new_dp = dp.copy()
    for i in range(X+1):
        if dp[i]:
            for j in range(i + a, min(X, i + a * b) + 1, a):
                new_dp[j] = True
    if new_dp[X]:
        flag = True
        break
    dp = new_dp.copy()

if flag:
    print("Yes")
else:
    print("No")