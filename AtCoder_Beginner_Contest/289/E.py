T = int(input())
for _ in range(T):
  N,M = map(int,input().split())
  L1 = list(map(int,input().split()))
  if L1[0] == L1[-1]:
    print(-1)
    for _ in range(M):
      a,b = map(int,input().split())
  else:
    Graph = [[] for _ in range(N)]
    for _ in range(M):
      a,b = map(int,input().split())
      Graph[a-1].append(b-1)
      Graph[b-1].append(a-1)
    seen = [-1]*(N**2)
    D = [[N-1]]
    seen[N-1] = 0
    while D:
      x = D.pop()
      L = []
      for l in x:
        a = l//N
        b = l%N
        for v in Graph[a]:
          for t in Graph[b]:
            if L1[v] != L1[t] and seen[v*N+t] == -1:
              seen[v*N+t] = seen[l]+1
              L.append(v*N+t)
      if L != []:
        D.append(L)
    print(seen[N**2-N])
      
      
    
    