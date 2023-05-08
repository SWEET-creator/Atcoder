import itertools

N, M = map(int, input().split())

S = []
T = {}
size = 0
for i in range(N):
    s = input()
    S.append(s)
    size += len(s)
    
for i in range(M):
    t = input()
    T.append(t)

c_list = itertools.permutations(S, N)

bar_num = N-1
bar_add = 0
flag = False

def binary_search(data, v):
    l = 0
    r = len(data)-1
    while l <= r:
        mid = (l + r)//2
        if data[mid] == v:
            return mid
        elif data[mid] < v:
            l = mid + 1
        elif data[mid] > v:
            r = mid -1
    return -1

T.sort()

while size + bar_num + bar_add < 17:
    if N == 1 and bar_add > 0:
        break
    if bar_add > 0:
        all_patern = list(itertools.product(range(N-1), repeat=bar_add))
        for bar_pos_list in all_patern:
            bar_pos = [1]*(N-1)
            for pos in bar_pos_list:
                bar_pos[pos] += 1
            for c in c_list:
                x = ""
                for i in range(len(c)):
                    if i != 0:
                        for j in range(bar_pos[i-1]):
                            x += "_"
                    
                    x +=  c[i]
                if binary_search(T, x) == -1 and len(x) >= 3:
                    out = x
                    flag = True
                    break
            if flag:
                break
        if flag:
            break
    else:
        for c in c_list:
            x = ""
            for i in range(len(c)):
                if i != 0:
                    x += "_"
                x +=  c[i]
            if binary_search(T, x) == -1 and len(x) >= 3:
                out = x
                flag = True
                break
        if flag:
            break
    bar_add+= 1

if flag:
    print(out)
else:
    print(-1)
