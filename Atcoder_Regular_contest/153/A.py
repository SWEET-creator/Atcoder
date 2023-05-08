N = int(input())

ans = [1, 1, 0, 0, 0, 0, 0, 0, 0]

ans = 110000000
for i in range(N-1):
    ans+=10
    ans = list(str(ans))
    ans[8] = ans[6]
    ans[4] = ans[5]
    ans[0] = ans[1]
    ans = int("".join([str(x) for x in ans]))
    i+=1

print(ans)