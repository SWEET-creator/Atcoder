import collections
import math

K = int(input())

def main(K):
    for i in range(2*10**6)[1:]:
        K = int(K/math.gcd(K,i))
        if K == 1:
            return i
    return K

print(main(K))