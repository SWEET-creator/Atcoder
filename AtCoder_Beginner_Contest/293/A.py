S = list(input())

for i in range(len(S)//2):
    temp = S[2*(i+1)-2]
    S[2*(i+1)-2] = S[2*(i+1) -1]
    S[2*(i+1) -1] = temp

print("".join(S))