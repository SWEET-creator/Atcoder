N = int(input())
S = list(input())
for i in range(1, N): 
    flag = True
    for j in range(N-i):
        #print(i, j, S[j], S[j+i])
        if S[j] == S[j+i]:
            print(j)
            flag = False
            break
    if flag:
        print(j+1)