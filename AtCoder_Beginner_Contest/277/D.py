N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

B = [[]]
temp = 0
cnt = 0
flag = False
for i in range(N):
    if A[i] <= temp+1:
        if A[i] == M-1:
            flag = True
        B[cnt].append(A[i])
    else:
        cnt += 1
        B.append([A[i]])
    temp = A[i]
if flag and len(B) > 1:
    B.append(B[0] + B[-1])
    B.pop(0)
    B.pop(-2)

C = []
for b in B:
    C.append(sum(b))
print(sum(C) - max(C))