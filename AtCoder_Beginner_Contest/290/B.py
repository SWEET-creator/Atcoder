N, K = map(int, input().split())
S = list(input())

out = ["x" for i in range(N)]

j = 0
for i in range(N):
    if S[i] == "o":
        out[i] = "o"
        j += 1
        if j == K:
            print("".join(out))
            exit()
print("".join(out))