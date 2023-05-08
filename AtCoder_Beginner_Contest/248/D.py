from bisect import bisect_left, bisect_right

N = int(input())

A = list(map(int, input().split()))

Q = int(input())

pre = [[] for i in range(N+1)]

for i in range(0,N):
    pre[A[i]].append(i)

for i in range(Q):
    L, R, X = map(int, input().split())
    print(bisect_right(pre[X], R-1) - bisect_left(pre[X], L-1))