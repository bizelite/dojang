def collatz_between(first, last):
    max_cycle = 0
    for i in range(first, last+1):
        cycle = 1
        while i != 1:
            if i%2 == 0:
                i = i / 2
                cycle += 1
            else:
                i = i*3 + 1
                cycle += 1
        if cycle > max_cycle:
            max_cycle, cycle = cycle, max_cycle
    return first, last, max_cycle
<<<<<<< HEAD

if __name__ == '__main__':
    print(collatz_between(1, 10))
    print(collatz_between(100, 200))
    print(collatz_between(1, 100))
    
=======
    
>>>>>>> origin/master
