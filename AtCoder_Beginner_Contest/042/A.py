A, B, C = map(int, input().split())

ex = [3,5,7]

data = [A,B,C]

if data.count(5) == 2 and data.count(7) == 1:
    print("YES")
else:
    print("NO")