from collections import Counter

N = int(input())

A = list(map(int, input().split()))
out = [0]*N

c = Counter(A)

sorted_A = sorted(A)
rev_sorted_A = sorted_A[::-1]

data = {}
p = -1
count = 0
for i in range(len(A)):
    if p != rev_sorted_A[i]:
        p = rev_sorted_A[i]
        data[count] = p
        count += 1

for i in range(N):
    if i in data:
        print(c[data[i]])
    else:
        print(0)