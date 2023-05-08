S = []

for i in range(8):
    s = list(input())
    S.append(s)

c = ["a", "b", "c", "d", "e", "f", "g", "h"]

for i in range(8):
    for j in range(8):
        if S[i][j] == "*":
            print(c[j]+str(8-i))
            break