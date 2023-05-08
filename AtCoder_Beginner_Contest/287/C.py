import sys
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())

g = [[] for _ in range(N + 1)]
for i in range(M):
    u, v = map(int, input().split())
    g[u].append(v)
    g[v].append(u)

def dfs(u, visited, pre):
    
    visited[u] = True
    flag = True
    for v in g[u]:
        if not visited[v]:
            flag = dfs(v, visited, u)
        else:
            if v != pre:
                return False
    if flag:
        return True
    else:
        return False
visited = [False] * (N + 1)
pre = 0
flag = dfs(1, visited, pre)
if False in visited[1:] or not flag:
    print("No")
else:
    print("Yes")