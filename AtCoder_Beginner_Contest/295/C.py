N = int(input())

A = list(map(int, input().split()))

d = {}
for a in A:
    if a not in d:
        d[a] = 1
    else:
        d[a] += 1

val = list(d.values())
count = 0
for v in val:
    count += v//2

print(count)