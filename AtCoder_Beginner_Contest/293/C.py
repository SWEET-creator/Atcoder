H, W = map(int, input().split())

A = []
for i in range(H):
    a = list(map(int, input().split()))
    A.append(a)

visited = {}

def dfs(h, w, visited):
    global count
    visited[A[h][w]] = 0
    if h+1 < H:
        if A[h+1][w] not in visited:
            visited[A[h+1][w]] = 0
            dfs(h+1, w, visited)
            visited.pop(A[h+1][w])
        else:
            return
    if w+1 < W:
        if A[h][w+1] not in visited:
            visited[A[h][w+1]] = 0
            dfs(h, w+1, visited)
            visited.pop(A[h][w+1])
        else:
            return
    if h == H-1 and w == W-1:
        count += 1

count = 0
dfs(0,0, visited)

print(count)