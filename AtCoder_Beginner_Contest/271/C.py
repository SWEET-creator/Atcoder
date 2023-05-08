from collections import Counter

N = int(input())
a  = map(int, input().split())

c = Counter(a)
sorted_c = sorted(c)
stash = 0
for x in sorted_c:
    if x[1] > 1:
        stash+=1

