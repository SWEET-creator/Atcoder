s = input()
s = list(s)
n = -1
for i in range(len(s)):
    if(s[i] == "a"):
        n = i+1
print(n)