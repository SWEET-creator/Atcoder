N, x, y = map(int, input().split())
A = list(map(int, input().split()))

xset = set()
yset = set()

ax = []
ay = []
for i in range(N):
    if i % 2 == 0 and i != 0:
        ax.append(A[i])
    if i % 2 == 1:
        ay.append(A[i])

xset.add(A[0])
yset.add(0)

for i in range(len(ax)):
    tmpx = set()
    for k in xset:
        tmpx.add(k + ax[i]) 
        tmpx.add(k - ax[i])
    
    xset = tmpx

for i in range(len(ay)):
    tmpy = set()
    for k in yset:
        tmpy.add(k + ay[i]) 
        tmpy.add(k - ay[i])
    
    yset = tmpy
print(xset)
if x in xset and y in yset:
    print("Yes")
else:
    print("No")