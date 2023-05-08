A = list(input())
B = list(input())
C = list(input())

A.append("end")
B.append("end")
C.append("end")

turn = "a"
while A and B and C:
    if turn == "a":
        turn = A.pop(0)
    elif turn == "b":
        turn = B.pop(0)
    elif turn == "c":
        turn = C.pop(0)
    

if not A:
    print("A")
if not B:
    print("B")
if not C:
    print("C")