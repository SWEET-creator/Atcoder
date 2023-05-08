N = int(input())
e = [[] for _ in range(2*N)]
m = {}
for i in range(N):
    s,t = list(input().split())
    if s not in m:
        m[s] = len(m)
    if t not in m:
        m[t] = len(m)
    e[m[s]].append(m[t])
v = [-1] * (2*N)

for i in range(2*N):
    if v[i] >= 0:
        continue
    s = [i]
    while len(s) > 0:
        t = s[-1]
        s.pop()
        for ee in e[t]:
            if v[ee] == -1:
                s.append(ee)
            elif v[ee] < i:
                continue
            elif v[ee] == i:
                print("No")
                exit()
print("Yes")