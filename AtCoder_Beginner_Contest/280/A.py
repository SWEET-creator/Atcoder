H, W = map(int, input().split())

S = []
for i in range(H):
    S.append(list(input()))

count = 0
for s in S:
    for x in s:
        if x == "#":
            count += 1

print(count)