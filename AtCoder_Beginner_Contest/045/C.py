S = list(input())

n = len(S) - 1

out = int("".join(S))
for i in range(2 ** n):
    plus = []
    total = 0
    for j in range(n):  # このループが一番のポイント
        if ((i >> j) & 1):
            plus.append(j)
    
    if plus:
        cal_list = []
        prev = 0
        for p in plus:
            cal_list.append(int("".join(S[prev:p+1])))
            prev = p+1
        cal_list.append(int("".join(S[prev:])))
        out += sum(cal_list)
        
print(out)