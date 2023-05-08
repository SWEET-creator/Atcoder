S = list(input())

i = 1
for s in S:
    if not s.islower():
        print(i)
    i+=1
