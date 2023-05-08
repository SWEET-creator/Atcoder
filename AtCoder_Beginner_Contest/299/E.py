from collections import defaultdict 

N, M = map(int, input().split())

g = defaultdict(set)
for i in range(M):
    u, v = map(int, input().split())
    g[u].add(v)
    g[v].add(u)

K = int(input())

for i in range(K):
    p, d = map(int, input().split())

res = 'Yes'
color = [0 for i in range(N+1)]

def dfs(u, c, queue=[]):
    global res
    global color
    queue.append(u)

    for i in list(g[u]):
        if color[i] == c:
            res = "No"
            print("n",u,i)
        elif i not in queue:
            color[i] = c*-1
            dfs(i,-c,queue)


color[1] = 1
dfs(1,1)
print(res)