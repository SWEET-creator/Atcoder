K = int(input())

s = []
for i in range(K):
    s.append(chr(ord("A")+i))

print("".join(s))