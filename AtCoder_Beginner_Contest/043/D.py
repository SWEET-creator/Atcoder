s = list(input())

temp1 = s[0]
temp2 = s[1]
flag1 = False
for i in range(len(s))[2:]:
    if temp1 == temp2 or temp1 == s[i] or temp2 == s[i]:
        print(i, i+2)
        flag = True
        break
    temp1 = temp2
    temp2 = s[i]
if not flag:
    print(-1,-1)