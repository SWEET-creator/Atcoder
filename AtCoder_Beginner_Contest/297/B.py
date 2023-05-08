S = list(input())

B_pos = []
K_pos = 0
R_pos = []

for i in range(8):
    if S[i] == "B":
        B_pos.append(i)
    if S[i] == "K":
        K_pos = i
    if S[i] == "R":
        R_pos.append(i)

f = B_pos[0]%2 != B_pos[1]%2
g = R_pos[0] < K_pos and K_pos < R_pos[1]
if f and g:
    print("Yes")
else:
    print("No")