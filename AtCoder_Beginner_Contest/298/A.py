N = int(input())
S =list(input())

count = [0]*3
for s in S:
    if s == "o":
        count[0] += 1
    if s == "-":
        count[1] += 1
    if s == "x":
        count[2] += 1

if count[0] > 0 and count[2] == 0:
    print("Yes")
else:
    print("No")