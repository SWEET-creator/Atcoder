N = int(input())
A = list(map(int, input().split()))

pi = [False]*360

pi[0] = True
s = 0
for i in range(N):
    pi[(A[i]+s)%360] = True
    s += A[i]


ans = 0
pre = 0
out = []
for i in range(1,len(pi)):
    if pi[i]:
        out.append(i-pre)
        pre = i
out.append(360-pre)
print(max(out))