N , M = map(int, input().split())

a = list(map(int, input().split()))

g = [[] for i in range(N+1)]

for x in a:
    g[x].append(x+1)
    g[x+1].append(x)

def dfs(v, visited):
    global w
    visited[v] = True
    w.append(v)
    for i in g[v]:
        if not visited[i]:
            dfs(i, visited)

visited = [False]*(N+1)

visited[0] = True

out = []
while(False in visited):
    for i in range(N+1):
        if visited[i] == False:
            w = []
            dfs(i, visited)
            w.sort()
            out += w[::-1]
print(*out)