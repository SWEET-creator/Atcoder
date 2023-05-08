T = int(input())

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

for i in range(T):
    N, D, K = map(int, input().split())
    g = gcd(N, D)
    lcm = N // g
    if g == 1:
        print((K - 1)*D%N)
    else:
        print((K - 1)*D%N + (K-1)//lcm)