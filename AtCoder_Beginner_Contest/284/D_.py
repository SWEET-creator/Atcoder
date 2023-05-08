T  = int(input())

for _ in range(T):
    x = int(input())
    q = 2
    while q <= x**0.5:
        if(x%(q*q) == 0):
            print(x%(q*q))
            break
        q+=1
    p = x/(q*q)
    print(q,p)