N, X, Y = map(int, input().split())

r = [0 for i in range(N+1)]
b = [0 for i in range(N+1)]

r[N] = 1

while(N > 1):
    b[N] += r[N]*X
    r[N-1] += r[N] + b[N]
    b[N-1] += b[N]*Y
    N -= 1
print(b[1])