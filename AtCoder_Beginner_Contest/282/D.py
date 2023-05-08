import sys
sys.setrecursionlimit(3*10**5)

N, M = map(int, input().split())
v={}

color = [0] * N

for i in range(M):
    v1,v2=map(int,input().split())
    v1 -= 1
    v2 -= 1
    if v1 not in v:
        v[v1] = []
    if v2 not in v:
        v[v2] = []
    v[v1].append(v2)
    v[v2].append(v1)

def dfs(n, p, c):
    color[n] = c
    res = [0, 0]
    if c == 1:
        res[0] += 1
    else:
        res[1] += 1

    for u in v[n]:
        if color[u] == -c or u == p:
            continue
            
        if color[u] == c:
            return [-1,-1]
        
        ret = dfs(u, n, -c)
        if ret[0] == -1:
            return [-1,-1]
        res[0] += ret[0]
        res[1] += ret[1]
    
    return res



out = N*(N-1)//2 - M
for i in range(N):
    if not color[i]:
        res = dfs(i, -1, 1)
        if res[0] == -1:
            print(0)
            exit()
        out -= res[0]*(res[0]-1)//2
        out -= res[1]*(res[1]-1)//2


print(out)