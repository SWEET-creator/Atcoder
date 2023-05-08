N = int(input())
S = list(input())

enclose = False
temp = []
for i in range(N):
    if S[i] == "\"":
        if not enclose:
            for j in temp:
                S[j] = "."
            temp = []
            enclose = True
        else:
            temp = []
            enclose = False
    if S[i] == ",":
        temp.append(i)
        
if temp:
    for j in temp:
        S[j] = "."

print("".join(S))