N = int(input())
a = list(map(int, input().split()))

out = [0] * (2*N+2)
for i in range(1, N+1):
    out[2*i] = out[a[i-1]]+1
    out[2*i+1] = out[a[i-1]]+1

for i in range(1, len(out)):
    print(out[i])