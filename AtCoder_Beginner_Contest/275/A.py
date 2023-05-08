import numpy as np

n = int(input())
raw = input().split()
H = [int(x) for x in raw]

print(np.argmax(H)+1)