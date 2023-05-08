S = list(input())
T = list(input())

no_flag = True
for i in range(len(S)-len(T)+1):
    flag = True
    s_i = i
    for j in range(len(T)):
        if S[s_i] != T[j]:
            flag = False
            break
        s_i += 1
    if flag:
        print("Yes")
        no_flag = False
        break
if no_flag:
    print("No")

#21:16