N = int(input())

S = []
for i in range(N):
    S.append(input())

char_list = ["A" , "2" , "3" , "4" , "5" , "6" , "7" , "8" , "9" , "T" , "J" , "Q" , "K"]

flag = 1
for i in range(N):
    if not (list(S[i])[0] == "H" or list(S[i])[0] == "D" or list(S[i])[0] == "C" or list(S[i])[0] == "S"):
        flag = 0
        break

    second_flag = 0
    for x in char_list:
        if list(S[i])[1] == x:
            second_flag = 1
    if second_flag == 0:
        flag = 0
        break

    for j in range(N):
        if(i != j and S[i] == S[j]):
            flag = 0
            break
    
    if flag == 0:
        break


            
        

if flag == 1:
    print("Yes")
else:
    print("No")

#21:17