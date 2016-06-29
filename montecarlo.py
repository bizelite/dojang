import random

def pi(n):
    count = 0
    for i in range(n):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        if (x**2 + y**2) <= 1:
            count += 1
    return 4 * count / n

print(pi(56000))
print(pi(10000))
