N = 998244353

A, B, C, D, E, F = map(int, input().split())

A %= N
B %= N
C %= N
D %= N
E %= N
F %= N

print(((A*B%N)*C%N - (D*E%N)*F%N)%N)