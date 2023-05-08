N = int(input())

count = 0
for i in range(N):
    S = input()
    if S == "For":
        count += 1
if N/2 <= count:
    print("Yes")
else:
    print("No")