def d(n):
    return n + sum([int(x) for x in str(n)])

S = set(range(1, 5000))
A = set([d(n) for n in range(1, 5000)])
print(sum(S-A)