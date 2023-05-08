H, W = map(int, input().split())
A = []
B = []
for i in range(H):
    a = list(input())
    A.append(a)

for j in range(H):
    b = list(input())
    B.append(b)

for h in range(H):
    for w in range(W):
        flag = True
        for i in range(H):
            for j in range(W):
                if A[i][j] != B[i][j]:
                    flag = False
                    break

        if flag:
            print("Yes")
            exit()
        for i in range(H):
            head = A[i].pop(0)
            A[i].append(head)
    head = A.pop(0)
    A.append(head)

print("No")