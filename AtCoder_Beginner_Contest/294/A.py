N = int(input())

A = list(map(int, input().split()))

out = []
for a in A:
    if a%2 == 0:
        out.append(a)

print(*out)