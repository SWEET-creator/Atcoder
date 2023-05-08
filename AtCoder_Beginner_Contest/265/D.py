N, P, Q, R = map(int, input().split())
A = list(map(int, input().split()))

S = P + Q + R

x = 0
sum = 0
w = 0
for i in range(N):
    sum += A[i]
    while sum > S:
        sum -= A[x]
        x += 1
    if sum == S:
        w = i
        break

