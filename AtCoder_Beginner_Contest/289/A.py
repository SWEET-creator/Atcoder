s = list(input())
out  = [str(0) if int(x) else str(1) for x in s]

print("".join(out))