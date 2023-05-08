N = int(input())

A = list(map(int, input().split()))

Q = int(input())

x = -1
B = {}
for i in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        x  = q[1]
        B = {}
    elif q[0] == 2:
        if q[1] -1 not in B:
            B[q[1]-1] = 0
        B[q[1]-1] += q[2]
    else:
        if q[1] -1 not in B:
            B[q[1]-1] = 0
        if x == -1:
            print(A[q[1]-1] + B[q[1]-1])
        else:
            print(x + B[q[1]-1])
