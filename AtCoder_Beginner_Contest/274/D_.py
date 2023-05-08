n,x,y = map(int, input().split())
 
a = list(map(int, input().split()))
ax = []
ay =[]
xset = set()
yset = set()
 
for i in range(n):
    if i % 2 ==0 and i !=0:
        ax.append(a[i])
    if i % 2 !=0 and i!=0:
        ay.append(a[i])
 
xset.add(a[0])
yset.add(0)
 
for i in range(len(ax)):
    tmpx = set()
    for k in xset:
        tmpx.add(k + ax[i])
        tmpx.add(k-ax[i])
    
    xset = tmpx
    
for i in range(len(ay)):
    tmpy = set()
    for k in yset:
        tmpy.add(k + ay[i])
        tmpy.add(k-ay[i])
    
    yset = tmpy
 
judex = False
judey = False
 
print(xset)
if x in xset:
    judex = True
if y in yset:
    judey = True
 
if judex == True and judey == True:
    print("Yes")
else:
    print("No")