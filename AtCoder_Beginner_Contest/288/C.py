import sys
sys.setrecursionlimit(10**6)
N ,M = map(int, input().split())

g = [[] for i in range(N+1)]

for i in range(M):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)


visited = [False] * (N+1)

count = 0
def dfs(v, visited, pre):
    global count
    visited[v] = True
    for u in g[v]:
        if not visited[u]:
            dfs(u, visited, v)
        else:
            if u != pre:
                count += 1


for i in range(1, N+1):
    if not visited[i] and len(g[i]) > 0:
        dfs(i, visited, 0)

print(int(count/2))