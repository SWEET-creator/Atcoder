N = int(input())

A = []
for i in range(N):
    a = list(map(int, input().split()))
    A.append(a)

B = []
for i in range(N):
    b = list(map(int, input().split()))
    B.append(b)

for k in range(4):
    flag = True
    new = [[0]*N for i in range(N)]
    for i in range(N):
        for j in range(N):
            new[j][N-i-1] = A[i][j]
    for i in range(N):
        for j in range(N):
            if new[i][j] == 1:
                if B[i][j] != 1:
                    flag = False
                    break
    A = new
    if flag:
        print("Yes")
        exit()
print("No")

    