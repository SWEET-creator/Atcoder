N = int(input())

d = [1]*N

for x in range(2,N+1):
    i = 1
    while x*i < N:
        d[x*i] += 1
        i += 1

out = 0
y = N-1
for x in range(1,N):
    if x > y or x == y:
        break
    out += d[x]*d[y]
    y -= 1
out *= 2
if N%2 == 0:
    out += d[N//2]*d[N//2]

print(out)