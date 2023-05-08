K = int(input())

p_list = []
p = 2

k = K

while p*p <= k:
    count = 0
    while k%p == 0:
        k //= p
        count += 1
    if count > 0:
        p_list.append((p, count))
    p += 1
if k > 1:
    p_list.append((k,1))


def legendre(n,p):
    count = 0
    p2 = p
    while True:
        temp = n // p2
        if temp == 0:
            break
        count += temp
        p2 *= p
    return count

def isok(n):
    for p, e in p_list:
        if legendre(n,p) < e:
            return False
    return True

ng, ok = 1, k
while abs(ok - ng)>1:
    mid = (ok + ng)/2
    if isok(mid):
        ok = mid
    else:
        ng = mid
print(ok)
