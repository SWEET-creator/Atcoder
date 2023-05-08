N = int(input())

A = list(map(int, input().split()))

m = [[]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if A[i] == A[j]:
            m[i][j] = True

m = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        m[i][j] += 1