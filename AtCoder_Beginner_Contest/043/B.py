s = list(input())

out = []
for x in s:
    if x == "B":
        if out:
            out.pop(-1)
    else:
        out.append(x)

print("".join(out))