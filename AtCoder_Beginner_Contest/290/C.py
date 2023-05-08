N, K = map(int, input().split())

A = list(map(int, input().split()))

def MEX(x):
    x = list(set(x))
    x.sort()
    for i in range(len(x)):
        if x[i] != i:
            return i
    return len(x)

print(min(MEX(A), K))