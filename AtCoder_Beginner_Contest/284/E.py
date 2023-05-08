N, M = map(int, input().split())

g = {}
for _ in range(M):
    a, b = map(int, input().split())
    if a not in g:
        g[a] = []
    if b not in g:
        g[b] = []
    g[a].append(b)
    g[b].append(a)

K = 0
visited = [False] * (N + 1)
def dfs(v, visited):
    global K
    K += 1
    visited[v] = True
    if v not in g:
        return
    for _ in g[v]:
        if not visited[_]:
            dfs(_, visited)


dfs(1, visited)

print(min(K, 10**6))