N, P, Q, R, S = map(int, input().split())

A = list(map(int, input().split()))

swap1  = A[P-1:Q]
swap2  = A[R-1:S]

A[P-1:Q] = swap2
A[R-1:S] = swap1
print(*A)
