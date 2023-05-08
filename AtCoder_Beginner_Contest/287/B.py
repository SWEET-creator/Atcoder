N, M = map(int, input().split())

S = []
T = {}
for i in range(N):
    S.append(input())

for i in range(M):
    t = input()
    T[t] = 0

count = 0
for s in S:
    if s[3:] in T:
        count += 1

print(count)
