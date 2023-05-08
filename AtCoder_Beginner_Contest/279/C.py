import numpy as np
import collections
H, W = map(int, input().split())

s = []
t = []
for i in range(H):
    s.append(list(input()))
for i in range(H):
    t.append(list(input()))

s = np.array(s).T.tolist()
t = np.array(t).T.tolist()

yes_flag = True
s = list(map(lambda x: "".join(x),s))
t = list(map(lambda x: "".join(x),t))
t_c = collections.Counter(t)

for x in s:
    flag = True
    if x in t_c:
        if t_c[x] == 0:
            print("No")
            yes_flag = False
            break
        else:
            t_c[x] -= 1
    else:
        print("No")
        yes_flag = False
        break

if yes_flag:
    print("Yes")

#21:50