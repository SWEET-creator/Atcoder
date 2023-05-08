import bisect
import math

N = int(input())


def eratosthenes(n):
  arr = [True] * (n + 1)
  arr[0], arr[1] = False, False
  i = 2
  while i * i <= n:
    if arr[i]:
      for x in range(i, n // i + 1):
        arr[i*x] = False
    i += 1
  primes = []
  for j in range(n + 1):
    if arr[j]: primes.append(j)
  return primes

a = 2
b = 3
c = 2
max_c = 2
while(N >= a**2 *b* (max_c**2)):
    max_c += 1

l = eratosthenes(max_c)

ans = 0
print(l)
for i in range(len(l)):
    c = l[i]
    for j in range(i):
        b = l[j]
        

print(ans)