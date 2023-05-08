N = int(input())

S = list(input())

watched = {}
rl = 0
ud = 0
watched[str(rl)+str(ud)] = 0
for x in S:
    if x == "R":
        rl += 1
    elif x == "L":
        rl -= 1
    elif x == "U":
        ud += 1
    else:
        ud -= 1

    if str(rl)+str(ud) not in watched:
        watched[str(rl)+str(ud)] = 0
    else:
        print("Yes")
        exit()

print("No")