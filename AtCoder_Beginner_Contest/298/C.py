N = int(input())
Q = int(input())

i_box = [[] for _ in range(2*10**5+1)]
box = [[] for _ in range(N+1)]

for i in range(Q):
    q = list(map(int,input().split()))
    if q[0] == 1:
        i = q[1]
        j = q[2]
        box[j].append(i)
        i_box[i].append(j)
    
    elif q[0] == 2:
        i = q[1]
        box[i].sort()
        print(*box[i])
        
    else:
        i = q[1]
        i_box[i] = list(set(i_box[i]))
        i_box[i].sort()
        print(*i_box[i])