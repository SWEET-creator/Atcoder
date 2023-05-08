N, K = map(int, input().split())

d = []
for i in range(N):
    S = input()
    if i < K:
        end_flag = False
        if len(d) == 0:
            d.append(S)
        else:
            for X in d:
                s = list(S)
                x = list(X)
                flag = False
                for i in range(min(len(s), len(x))):
                    if s[i] != x[i]:
                        flag = True
                        if s[i] < x[i]:
                            d.insert(d.index(X), S)
                            end_flag = True
                            break
                        else:
                            break
                if not flag:
                    if len(s) < len(x):
                        d.insert(d.index(X), S)
                        end_flag = True
                if end_flag:
                    break
            if not end_flag:
                d.append(S)

for x in d:
    print(x)