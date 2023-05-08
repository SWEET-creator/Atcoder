N, M = map(int, input().split())

S = [_ for _ in range(2**11-1)]

A = []
for i in range(M):
    C = int(input())
    a = set(map(int, input().split()))
    b = [0 for _ in range(10)]
    for x in a:
        b[10-x] = 1
    b = int("".join(list(map(str, b))), 2)
    A.append(b)

dp = [[0]*(M+1) for _ in range(len(S)+1)]

dp[0][0] = 1

for i in range(len(S)):
    for j in range(M):
        dp[i][j+1] += dp[i][j]
        dp[i | A[j]][j+1] += dp[i][j]
    
print(dp[2**N-1][M])