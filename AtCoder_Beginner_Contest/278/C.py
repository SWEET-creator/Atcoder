N, Q = map(int, input().split())

member = {}
for i in range(Q):
    t, a, b = map(int, input().split())
    if t == 1:
        if a not in member:
            member[a] = {}
        member[a][b] = 0

    elif t == 2:
        if a not in member:
            member[a] = {}
        if b in member[a]:
            del member[a][b]
    else:
        if a in member and b in member:
            if (b in member[a]) and (a in member[b]):
                print("Yes")
            else:
                print("No")
        else:
            print("No")