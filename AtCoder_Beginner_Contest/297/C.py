H, W = map(int, input().split())

out = []
for _ in range(H):
    s = list(input())
    o = []
    flag = True
    for j in range(1,W):
        if s[j] == "T" and s[j-1] == "T":
            if flag:
                o.append("PC")
                flag = False 
            else:
                flag = True
                if j == W-1:
                    o.append(s[j])
        else:
            if not flag:
                flag = True
                if j == W-1:
                    o.append(s[j])
            else:
                o.append(s[j-1])
                if j == W-1:
                    o.append(s[j])
        
    out.append("".join(o))

for o in out:
    print(o)