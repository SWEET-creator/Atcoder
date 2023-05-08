N , X = map(int, input().split())

A = list(map(int, input().split()))

def binary_search(arr, low, high, x):
    if high >= low:
 
        mid = (high + low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, high, x)
 
    else:
        return -1
    
A.sort()
for a in A:
    if binary_search(A, 0, N-1, a - X) != -1:
        print("Yes")
        exit()
    if binary_search(A, 0, N-1, a + X) != -1:
        print("Yes")
        exit()

print("No")
