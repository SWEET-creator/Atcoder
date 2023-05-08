N = int(input())

data = []
G = {}
for i in range(N):
    A, B = map(int, input().split())
    if A in G:
        G[A].append(B)
    else:
        G[A] = []
        G[A].append(B)
    if B in G:
        G[B].append(A)
    else:
        G[B] = []
        G[B].append(A)

def DFS(s):
    m = s
    q = [s]
    watched = {}
    while(q):
        next = q.pop()
        if next in G:
            for n in G[next]:
                if n not in watched:
                    m = max(m, n)
                    q.append(n)
                    watched[n] = 0

    return m


print(DFS(1))