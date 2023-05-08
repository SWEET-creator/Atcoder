import heapq
N, K = map(int, input().split())
A = list(map(int, input.split()))

q = [0]

while K>0:
    l = heapq.heappop(q)
    while q and l == q[0]:
        l = heapq.heappop(q)
    for ai in A:
        heapq.heappush(q, l + ai)
    K -= 1