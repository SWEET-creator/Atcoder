S = list(input())

l = len(S)
ans = 0
for s in S:
    ans += (ord(s) - ord('A') + 1) * (ord('Z')-ord('A')+1)**(l-1)
    l -= 1
print(ans)