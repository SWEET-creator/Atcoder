N = int(input())

A = list(map(int, input().split()))

sig = []

for i in range(N):
    s = []
    for j in range(N):
        if i == 0:
            s.append(A[j])
        else:
            s.append(A[sig[i-1][j]-1])
    sig.append(s)

print(len(list(set(sig))))