import math

A, B = map(int, input().split())

cnt = 0
while(True):
    if A < B:
        A, B = B, A
    if A % B == 0:
        cnt += A//B - 1
        break
    cnt += A//B
    A %= B

print(cnt)