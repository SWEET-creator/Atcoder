N, K = map(int,input().split())
a = list(map(int, input().split()))

class C:
    def __init__(self, i):
        self.id = i
    def __lt__(self, other):
        return a[self.id] < a[other.id]

order = [C(i) for i in range(N)]
order.sort()

answer = [K // N for i in range(N)]
for i in range(K % N):
    answer[order[i].id] += 1
for x in answer:
    print (x)