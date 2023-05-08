N, M, K = map(int, input().split())

cnt = 0

s = {}
s["11"] = 0
for k in range(0,K-2):
    next_s = {}
    for x in s.keys():
        next_s[x] = 0
    for x in s.keys():
        for n in range(N):
            next_s[str(int(x) + 10**n)] = 0
    for x in next_s.keys():
        s[x] = 0

print(len(s))