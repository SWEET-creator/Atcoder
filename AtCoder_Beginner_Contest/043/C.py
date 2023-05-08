N = int(input())

a = list(map(int, input().split()))
x = int(sum(a)/N)
out = []
for i in [-1,0,1]:
    y = sum(list(map(lambda ai: (ai - x+i)**2, a)))
    out.append(y)

print(min(out))