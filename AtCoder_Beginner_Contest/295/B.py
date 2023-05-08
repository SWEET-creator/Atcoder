import numpy as np

R, C = map(int, input().split())

B = []

for i in range(R):
    b = list(input())
    B.append(b)

out = [[B[i][j] for j in range(C)] for i in range(R)]

for i in range(R):
    for j in range(C):
        if B[i][j] == ".":
            continue
        elif B[i][j] == "#":
            continue
        else:
            num = int(B[i][j])
            for k in range(num+1):
                for l in range(num+1 - k):
                    aa = np.clip(i + k, 0, R - 1)
                    bb = np.clip(i - k, 0, R - 1)
                    cc =np.clip(j + l, 0, C - 1)
                    dd = np.clip(j - l, 0, C - 1)
                    out[aa][cc] = "."
                    out[bb][cc] = "."
                    out[aa][dd] = "."
                    out[bb][dd] = "."
for o in out:
    print("".join(o))
