a = list()
for i in range(4):
    a.append(input())
b = ['H', '2B', '3B', 'HR']

print("Yes" if set(a) == set(b) else "No")
