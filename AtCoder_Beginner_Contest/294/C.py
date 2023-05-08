N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = []
for a in A:
    C.append([a, 0])

for b in B:
    C.append([b,1])

C.sort()

out_A = []
out_B = []
for i in range(N+M):
    if C[i][1] == 0:
        out_A.append(i+1)
    else:
        out_B.append(i+1)

print(*out_A)
print(*out_B)