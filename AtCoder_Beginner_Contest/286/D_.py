N, X = map(int, input().split())
 
bit = 1
for _ in range(N):
    A, B = map(int, input().split())
    for _ in range(B):
        bit |= bit << A
 
print("Yes" if bit >> X & 1 else "No")