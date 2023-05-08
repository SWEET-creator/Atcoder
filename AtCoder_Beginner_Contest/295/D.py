S = list(input())

patern = [0]*1024

a = 1023
patern[a] += 1
for s in S:
    num = int(s)
    a ^= 2**num
    patern[a] += 1

count = 0
for p in patern:
    count += int(p*(p-1)/2)
print(count)