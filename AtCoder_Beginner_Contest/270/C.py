import sys
sys.setrecursionlimit(10**6)

from collections import deque

N, X, Y = map(int, input().split())

g = {}
for i in range(N-1):
    u, v = map(int, input().split())
    if u not in g:
        g[u] = []
    if v not in g:
        g[v] = []
    g[u].append(v)
    g[v].append(u)

que = deque()

def dfs(u, last = -1):
    que.append(u)
    if u == Y:
        print(*que)
        exit()
    
    for v in g[u]:
        if v == last:
            continue

        dfs(v, u)
        que.pop()

dfs(X)