N = int(input())
S = list(input())

count = 0
ans = []
for i in range(N):
    s = S[i]
    if s == "o":
        count += 1
    elif s == "-":
        if count != 0:
            ans.append(count)
            count = 0

if len(ans):
    print(max(ans))
else:
    print(-1)