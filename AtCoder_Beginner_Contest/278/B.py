h, m = map(int, input().split())

if h < 6 or (h>=10 and h < 16) or (h>=20 and m<40):
    print(h, m)
else:
    while(1):
        if m < 59:
            m+=1
        else:
            m = 0
            if h < 23:
                h+=1
            else:
                h = 0
        if h < 6 or (h>=10 and h < 16) or (h>=20 and m<40):
            print(h, m)
            break
