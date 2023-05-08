import numpy as np
import sys
sys.setrecursionlimit(10**7)

N = int(input())

m = [[False]*2001 for i in range(2001)]
for i in range(N):
    x, y = map(int, input().split())
    m[x+1000][y+1000] = True
    
g = {}
visited = {}
for i in range(2001):
    for j in range(2001):
        if m[i][j]:
            u = i*2001 + j
            visited[u] = False
            search_list = [[i-1,j-1], [i-1, j],[i, j-1], [i, j+1],  [i+1, j], [i+1, j+1]]
            for s in search_list:
                if 0 > s[0] or 0 > s[1] or s[0] > 2000 or s[1] > 2000:
                    continue
                if m[s[0]][s[1]]:
                    v = s[0]*2001 + s[1]
                    if u not in g:
                        g[u] = []
                    if v not in g:
                        g[v] = []
                    g[u].append(v)
                    g[v].append(u)
                    visited[v] = False

def dfs(u, visited):
    visited[u] = True

    for v in g[u]:
        if not visited[v]:
            dfs(v, visited)

count = 0
for k in visited.keys():
    if not visited[k]:
        if k not in g:
            count += 1
            continue
        dfs(k, visited)
        count += 1

print(count)