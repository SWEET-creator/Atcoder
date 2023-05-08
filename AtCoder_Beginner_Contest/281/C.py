N, T = map(int, input().split())

A = list(map(int, input().split()))

one_loop = sum(A)

r = T%one_loop

t_num = 0
while(True):
    if r - A[t_num] < 0:
        print(t_num+1, r)
        break
    r -= A[t_num]
    t_num += 1
