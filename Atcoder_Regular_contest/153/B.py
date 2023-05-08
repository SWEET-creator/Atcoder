H, W = map(int, input().split())

A = []
B = [[j for j in range(W)] for i in range(H)]
for h in range(H):
    A.append(list(input()))


Q = int(input())
h0, h1, w0, w1 = 0, 1, 0, 1
for q in range(Q):
    a, b = map(int, input().split())
    h0 = a - h0
    h1 = h1 - a
    w0 = w0 - b
    w1 = w1 - b

for a in A:
    print("".join(a))