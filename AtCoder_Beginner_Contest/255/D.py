N, Q = map(int, input().split())

A = list(map(int, input().split()))

s = sum(A)
min_num = min(A)
max_num = max(A)
for _ in range(Q):
    q = int(input())
    if min_num < q and q < max_num:
        print(s+N*min_num - q*N)
    else:
        print(abs(s - q*N))