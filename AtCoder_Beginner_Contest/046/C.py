N = int(input())

t_list = []
a_list = []
for i in range(N):
    t, a = map(int, input().split())
    t_list.append(t)
    a_list.append(a)

T = 0
A = 0
for i in range(N):
    t = t_list[i]
    a = a_list[i]
    if i == 0:
        T = t
        A = a
    else:
        if (T/t != A/a):
            if (T/t > A/a):
                A = int(T*(a/t))
            else:
                T = int(A*(t/a))
        while(T/t != A/a):
            if (T/t > A/a):
                A += 1
            else:
                T += 1
print(T+A)