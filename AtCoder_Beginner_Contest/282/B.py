N, M = map(int, input().split())
s = [list(input()) for _ in range(N)]

count = 0
for i in range(N):
    for j in range(i+1, N):
        flag = True
        for k in range(M):
            if s[i][k] == "x" and s[j][k] == "x":
                flag = False
                break
        if flag:
            count += 1
        
print(count)