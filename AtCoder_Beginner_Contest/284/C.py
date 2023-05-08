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

visited = [False] * (N + 1)
def dfs(v, visited):
    visited[v] = True
    if v not in g:
        return
    for _ in g[v]:
        if not visited[_]:
            dfs(_, visited)

ans = 0
for i in range(1, N+1):
    if not visited[i]:
        dfs(i, visited)
        ans += 1

print(ans)