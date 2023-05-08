N = int(input())
W = input().split()

check = ["and", "not", "that", "the", "you"]
for w in W:
    if w in check:
        print("Yes")
        exit()

print("No")