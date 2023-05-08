H, W = map(int, input().split())

A = []
for _ in range(H):
    A.append(list(map(int, input().split())))

out = []
for a_h in A:
    sub = []
    for a in a_h:
        if a == 0:
            sub.append(".")
        else:
            sub.append(chr(a+64))
    out.append(sub)

for o in out:
    print("".join(o))