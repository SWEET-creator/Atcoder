T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int,input().split()))
    A = list(map(lambda x: x%2 != 0, A))
    print(A.count(True))