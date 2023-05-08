N, X = map(int, input().split())
raw = input()
raw = raw.split()
raw = [int(x) for x in raw]
for i in range(N):
    if X == raw[i]:
        print(i+1)