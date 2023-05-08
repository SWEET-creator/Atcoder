N = int(input())

M = 998244353

k = 9
ans = 0
s = 0
while N > k:
    N -= k
    ans += k*(k+1)//2
    ans %= M
    k *= 10

ans += N*(N+1)//2
ans %= M

print(ans)