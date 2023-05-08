S = list(input())
T = list(input())


def counting(L):
    temp = L[0]
    e = []
    n = []
    count = 1
    for l in L[1:]:
        if temp == l:
            count +=1
        else:
            e.append(temp)
            n.append(count)
            temp = l
            count = 1
    e.append(l)
    n.append(count)
    return e, n

e_s, n_s = counting(S)
e_t, n_t = counting(T)

f1 = e_s == e_t
if f1:
    for i in range(len(n_t)):
        if n_s[i] == n_t[i]:
            continue
        elif n_s[i] > n_t[i]:
            print("No")
            exit()
        else:
            if n_s[i] < 2:
                print("No")
                exit()
    print("Yes")
else:
    print("No")
