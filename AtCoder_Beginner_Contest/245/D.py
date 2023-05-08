N, M = map(int, input().split())

X = 256

A = 0
Xⁿ = 1
for a in map(int, input().split()):
    A += a * Xⁿ
    Xⁿ *= X

C = 0
Xⁿ = 1
for c in map(int, input().split()):
    C += c * Xⁿ
    Xⁿ *= X

B = C // A
b = []
print("A", A)
print("C", C)
while B != 0:
    x = B % X
    if x > 100:
        x -= X
    b.append(x)
    print(B)
    B = (B - x) // X
    print(B)

print(*b)
