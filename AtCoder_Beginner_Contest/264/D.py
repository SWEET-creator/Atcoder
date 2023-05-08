S = list(input())

dic = {"a":1, "t":2, "c":3, "o":4, "d":5, "e":6, "r":7}
a = []
for s in S:
    a.append(dic[s])
m  = len(S)
count = 0
while m > 1:
    for j in range(0,m-1):
        if a[j] < a[j+1]:
            continue
        else:
            a[j], a[j+1] = a[j+1], a[j]
            count += 1
    m -= 1

print(count)

