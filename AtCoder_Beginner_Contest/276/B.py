raw = input()
raw = raw.split()
N = int(raw[0])
M = int(raw[1])

data = []

for i in range(M):
    raw = input()
    raw = raw.split()
    raw = [int(x) for x in raw]
    data.append(raw)

map = {}
for i in range(M):
    if(data[i][0] in map):
        map[data[i][0]].append(data[i][1])
    else:
        map[data[i][0]] = []    
        map[data[i][0]].append(data[i][1])
    
    if data[i][1] in map:
        map[data[i][1]].append(data[i][0])
    else:
        map[data[i][1]] = []
        map[data[i][1]].append(data[i][0])

for i in range(1,N+1):
    if(i in map):
        ans = map[i]
        ans.sort()
        ans.insert(0,len(ans))
        print(*ans)
    else:
        print(0)

