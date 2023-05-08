import itertools 
 
H1,W1 = map(int, input().split())
A = []

for i in range(H1):
    A.append(list(map(int, input().split())))

H2,W2 = map(int, input().split())

B = []

for i in range(H2):
    B.append(list(map(int, input().split())))

for h in itertools.combinations(range(H1),H2):
    for w in itertools.combinations(range(W1),W2):
        ans = True
        for i in range(H2):
            for j in range(W2):
                if A[h[i]][w[j]] != B[i][j]:
                    ans = False
        if ans:
            print("Yes")
        exit()

print("No")