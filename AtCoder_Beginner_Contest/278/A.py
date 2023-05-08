N, K = map(int,input().split())

A = input().split()
A = [int(_) for _ in A]

for i in range(K):
    A.pop(0)
    A.append(0)

print(*A)