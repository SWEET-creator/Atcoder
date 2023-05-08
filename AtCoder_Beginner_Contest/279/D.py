A, B = map(int, input().split())

def f(g):
    return B * (g-1) + A/pow(g,0.5)

def diff_f(g):
    return B - A/(2*pow(g,1.5))

def numerical_diff(f, x):
    h = 1e-4
    return (f(x+h) -f(x-h))/(2*h)

g = 0
g_next = 1
lr = 1e-3

while(g_next - g > 1e-10):
    g = g_next
    g_next -= lr * diff_f(g)

g = g_next
g = int(g)
if g <= 0:
    print(f(1))
else:
    if f(g) < f(g+1):
        print(f(g))
    else:
        print(f(g+1))
        