N = int(input())
S = list(map(int, input().split()))

A = [0]*N
A[0] = S[0]
A_sum = A[0]

for i in range(N)[1:]:
    A[i] = S[i] - A_sum
    A_sum += A[i]

print(*A)