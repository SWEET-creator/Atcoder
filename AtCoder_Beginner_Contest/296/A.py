N = int(input())

S = list(input())

temp = S[0]
for s in S[1:]:
    if temp == s:
        print("No")
        exit()
    temp = s

print("Yes")