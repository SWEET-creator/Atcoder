import sys
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())

g = {}

for i in range(M):
    u, v = map(int, input().split())
    if u-1 not in g:
        g[u-1] = []
    if v-1 not in g:
        g[v-1] = []
    g[u-1].append(v-1)
    g[v-1].append(u-1)

def dfs(u, visited):
    global n, m
    visited[u] = True
    n += 1

    for v in g[u]:
        m += 1
        if not visited[v]:
            dfs(v, visited)

visited = [False]*N
for u in range(N):
    if not visited[u]:
        if u in g:
            n = 0
            m = 0
            
            dfs(u, visited)
            if n != m/2:
                print("No")
                exit()
        else:
            print("No")
            exit()

print("Yes")