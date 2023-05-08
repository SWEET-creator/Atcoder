N = int(input())

a = list(map(int, input().split()))

M = int(input())

b = set(map(int, input().split()))

X = int(input())

dp = [False for _ in range(X+1)]

dp[0] = True
for i in range(0, X+1):
    for j in range(N):
        if dp[i] and i + a[j] <= X and (i not in b):
            dp[i + a[j]] = True
        
if dp[X]:
    print('Yes')
else:
    print('No')