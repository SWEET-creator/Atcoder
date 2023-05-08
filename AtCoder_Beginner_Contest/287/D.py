S = input()
T = input()

pre = [False] * (len(T) + 1)
suf = [False] * (len(T) + 1)

def isMatch(a,b):
    if a == "?" or b == "?":
        return True
    elif a == b:
        return True
    else:
        return False

pre[0] = True
for i in range(len(T)):
    if isMatch(S[i],T[i]):
        pre[i+1] = True
    else:
        break

suf[len(T)] = True
for j in range(len(T)):
    if isMatch(S[-j-1],T[-j-1]):
        suf[-j-2] = True
    else:
        break
    

for i in range(len(T)+1):
    if pre[i] and suf[i]:
        print("Yes")
    else:
        print("No")
