A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
D = list(map(int, input().split()))

def dis(a,b):
    return pow((a[0]-b[0])**2 + (a[1]-b[1])**2, 0.5)

def isYes(A,B,C,D):
    a = (A[1] - B[1])/(A[0] - B[0])
    b = A[1] - a*A[0]

    c = (C[1] - D[1])/(C[0] - D[0])
    d = C[1] - c*C[0]

    if a == c:
        print("Yes")
        exit()

    x = (d-b)/(a-c)
    y = a*x+b
    inter = [x,y]

    #f1 = max(dis(A,inter), dis(B,inter)) < dis(A,B) and max(dis(C,inter), dis(D,inter)) < dis(C,D)
    f2 = False
    for p in [A,B,C,D]:
        if p == inter:
            f2 = True

    if f2:
        print("Yes")
        exit()

if A[0] != B[0] and C[0] != D[0]:
    isYes(A,B,C,D)
if A[0] != C[0] and B[0] != D[0]:
    isYes(A,C,B,D)
if A[0] != D[0] and B[0] != C[0]:
    isYes(A,D,B,C)

print("No")