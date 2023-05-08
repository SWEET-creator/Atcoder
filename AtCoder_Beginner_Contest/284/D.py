T  = int(input())

for _ in range(T):
    x = int(input())
    q = 2
    while q*q*2 <= x:
        if x % q == 0:
            break
        q += 1
    p = x // q**2
    if q**2 * p == x:
        print(q, p)
    else:
        p = x // q
        print(int(pow(p,1/2)), q)