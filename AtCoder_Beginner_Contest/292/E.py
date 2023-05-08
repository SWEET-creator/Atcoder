N, M = map(int, input().split())

g = {}

for _ in range(M):
    u, v = map(int, input().split())
    if u-1 not in g:
        g[u-1] = []
    g[u-1].append(v-1)


def dfs(t, u, visited):
    visited[u] = True

    for v in g[u]:
        if v in g[t]:
            dfs(u, v ,visited)
        else:

visited = [False]*N

for u in range(N):
    for v in range(N):
        if not visited[v] and v not in g[u]:
            g_ = g
            g_[u].append(v)
            dfs(u, visited)
