N, Q = map(int, input().split())

even = [list(map(int, input().split())) for _ in range(Q)]
p = [0]*(N+1)
for e in even:
    if e[0] == 1:
        p[e[1]] += 1
    elif e[0] == 2:
        p[e[1]] = 2
    else:
        if p[e[1]] > 1:
            print("Yes")
        else:
            print("No")
