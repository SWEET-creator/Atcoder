N = int(input())
A = list(map(int, input().split()))
Q = int(input())

q = [list(map(int, input().split())) for _ in range(Q)]

for query in q:
    if query[0] == 1:
        A[query[1]-1] = query[2]
    elif query[0] == 2:
        print(A[query[1]-1])