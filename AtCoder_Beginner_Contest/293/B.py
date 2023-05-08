N = int(input())
A = list(map(int, input().split()))

K = [False]*N

for i in range(N):
    if not K[i]:
        K[A[i] - 1] = True
    
out = []
for i in range(N):
    if not K[i]:
        out.append(i+1)

print(len(out))
print(*out)