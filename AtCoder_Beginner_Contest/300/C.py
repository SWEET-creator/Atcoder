import numpy as np

H, W  = map(int, input().split())
C = []

for i in range(H):
    c = list(input())
    C.append(c)




def is_s(x):
    if x == "#":
        return True
    else:
        return False

d = []
for x in range(H):
    for y in range(W):
        if  is_s(C[np.clip(x + 1, 0, H-1)][np.clip(y + 1, 0, W-1)]) and is_s(C[np.clip(x-1, 0, H-1)][np.clip(y+1, 0, W-1)]) and is_s(C[np.clip(x - 1, 0, H-1)][np.clip(y - 1, 0, W-1)]) and is_s(C[np.clip(x+1, 0, H-1)][np.clip(y-1, 0, W-1)]):
            d.append([x,y])
                
ans = [0] * H
ans[0] = len(d)
for n in range(2, H+1):
    count = 0
    next_d = []
    for pos in d:
        x = pos[0]
        y = pos[1]
        if is_s(C[np.clip(x + n, 0, H-1)][np.clip(y + n, 0, W-1)]) and is_s(C[np.clip(x-n, 0, H-1)][np.clip(y+n, 0, W-1)]) and is_s(C[np.clip(x - n, 0, H-1)][np.clip(y - n, 0, W-1)]) and is_s(C[np.clip(x+n, 0, H-1)][np.clip(y-n, 0, W-1)]):
            count += 1
            next_d.append(pos)
    d = next_d.copy()

    ans[n-2] -= count
    ans[n-1] = count
print(*ans)