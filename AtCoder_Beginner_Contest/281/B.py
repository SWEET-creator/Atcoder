S = list(input())

def func(S):
    if len(S) != 8:
        print("No")
        return
    if not S[0].isalpha():
        print("No")
        return
    for s in S[1:-1]:
        if s.isalpha():
            print("No")
            return
    if 100000 > int("".join(S[1:-1])) or int("".join(S[1:-1])) >  999999:
        print("No")
        return
    if not S[-1].isalpha():
        print("No")
        return
    print("Yes")
    return
func(S)