import math
S = list(str(input()))

temp = S[0]
count = 0
for s in S:
    if temp == "0" and s == "0":
        count += 1
        temp = None
    else:
        temp = s
print(len(S)-count)