N = int(input())
S = list(input())

ans = []
flag = False
for i in range(N):
    if flag:
        flag = False
        continue
    if i < N-1:
        if S[i] == "n" and S[i+1] == "a":
            ans.append("nya")
            flag = True
        else:
            ans.append(S[i])
    else:
        ans.append(S[i])

print("".join(ans))