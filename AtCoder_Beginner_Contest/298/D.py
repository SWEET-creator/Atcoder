import queue

Q = int(input())

M = 998244353

qu = queue.Queue()
qu.put(1)
ans = []
s = 1

for i in range(Q):
    query = list(map(int, input().split()))
    q = query[0]
    if q == 1:
        x = int(query[1])
        qu.put(x)
        s = (s * 10 + x)%M
    elif q == 2:
        l = qu.get()
        print("l",l)
        s = (s - l*pow(10, qu.qsize(), M))%M

    elif q == 3:
        ans.append(s)
    print(s)

for s in ans:
    print(s)