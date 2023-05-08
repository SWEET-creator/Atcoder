N, A, B = map(int, input().split())
S = list(input())

if N%2 == 0:
    first = S[:int(N/2)]
    later = S[int(N/2):][::-1]
else:
    first = S[:int(N/2)+1]
    later = S[int(N/2)+1:][::-1]

c = []
min_v = 0
for i in range(N):
    count = 0
    ans = A * i
    if min_v < ans:
        continue
    for j in range(len(later)):
        if first[j] != later[j]:
            count += 1
    ans += B * count
    c.append(ans)
    if i == 0:
        min_v = ans
    else:
        min_v = min(min_v, ans)

    later.insert(0,first.pop(0))
    first.append(later.pop(-1))
        
print(min(c))