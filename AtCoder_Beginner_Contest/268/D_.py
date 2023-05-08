import itertools
N =3
ss = 13

bar = list(itertools.combinations(range(16-ss+1), N))

print(bar)