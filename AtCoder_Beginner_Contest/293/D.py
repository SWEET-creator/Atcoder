N, M = map(int, input().split())

g = {}
for i in range(M):
    data = input().split()
    a = int(data[0]) - 1
    b = data[1]
    c = int(data[2]) - 1
    d = data[3]
    if a not in g:
        g[a] = []
    if c not in g:
        g[c] = []
    if b == "R":
        if d == "R":
            if a < c:
                g[a].append(c)
            else:
                g[c].append(a)
        else:
            g[a].append(c)
    else:
        if d == "B":
            if c < a:
                g[a].append(c)
            else:
                g[c].append(a)
        else:
            g[c].append(a)

def dfs(u, visited):
    global flag
    visited[u] = True

    for v in g[u]:
        if not visited[v]:
            dfs(v, visited)
        else:
            flag = True

visited = [False]*N
c = 0
nc = 0
for i in range(N):
    if not visited[i]:
        if i in g:
            if g[i]:
                flag = False
                dfs(i, visited)

                if flag:
                    c += 1
                else:
                    nc += 1
        else:
            nc += 1

print(c,nc)