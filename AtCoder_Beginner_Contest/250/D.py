

N = int(input())

max_q = 0
for i in range(2,int(pow(N, 1/3))+1):
    if N%(i ** 3) == 0:
        max_q = i
    
count = 0

def eratosthenes(n):
    is_prime = [False, False] + [True] * (n-1)
    for p in range(2, n+1):
        if not(is_prime[p]):
            continue
        for k in range(p*2, n+1, p):
            is_prime[k] = False
    return is_prime

p_list = eratosthenes(max_q)

for q in range(2,max_q+1):
    if p_list[q]:
        for p in range(2,q):
            if p_list[p] and N >= p * (q**3):
                count += 1
            
print(count)