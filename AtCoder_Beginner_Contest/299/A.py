N = int(input())
S = list(input())

ans = []

for s in S:
    if s != ".":
        ans.append(s)

if ans == ["|", "*", "|"]:
    print("in")
else:
    print("out")