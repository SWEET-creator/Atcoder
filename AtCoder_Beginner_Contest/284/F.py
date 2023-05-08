N = int(input())
S = input()

flag = True
for i in range(N):
    A = S[:i]
    B = S[i:N+i]
    C = S[N+i:]
    if B[::-1] == A + C:
        print(A+C)
        print(i)
        flag = False
        break

if flag:
    print(-1)