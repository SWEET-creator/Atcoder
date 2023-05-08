N, K = map(int, input().split())

A = list(map(int, input().split()))
Q = int(input())

for i in range(Q):
    l, r = map(int, input().split())
    if sum(A[l-1:r])%K == 0:
        print("Yes")
    else:
        print("No")