S = list(input())
T = list(input())

def main(S, T):
    for i in range(len(S)):
        if S[i] != T[i]:
            return i+1
    return i+2

print(main(S, T))