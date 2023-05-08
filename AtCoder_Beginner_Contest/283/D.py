S = list(input())

flag = True

box = [[]]
temp = -1
for i in range(len(S)):
    s = S[i]
    if s.isalpha():
        if s in box[-1]:
            flag = False
            break
        box[-1].append(s)
    elif s == ")":
        box.pop()
    elif s == "(":
        box.append([])
        box[-1] = box[-2].copy()

if flag:
    print("Yes")
else:
    print("No")