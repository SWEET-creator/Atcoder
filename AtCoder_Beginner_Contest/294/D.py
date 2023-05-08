from collections import OrderedDict

N, Q = map(int, input().split())

a = [[i, 0] for i in range(N)]
last = 0
checked = [False for i in range(N+1)]
ans = 1
out = []

for i in range(Q):
    event = input().split()
    if len(event) == 1:
        eq = int(event[0])
    else:
        eq = int(event[0])
        v = int(event[1])
    if eq == 1:
        continue
                
    elif eq == 2:
        checked[v] = True

    elif eq == 3:
        while checked[ans]:
            ans += 1
        out.append(ans)
        

for o in out:
    print(o)
    