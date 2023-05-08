W, H, N = map(int, input().split())

s = [[1]*100 for _ in range(100)]
for i in range(N):
    x, y, a = map(int, input().split())
    if a == 1:
        for i in range(x):
            for _ in s[i]:
                _ = 1
    elif a == 2:
        for i in range(x,W):
            for _ in s[i]:
                _ = 1
    elif a == 3:
        for i in range(y):
            for _ in s[i]:
                _ = 1
    else:
        for i in range(y,H):
            for _ in s[i]:
                _ = 1























                

out = 0
for x in s:
    out += sum(x)

print(s)