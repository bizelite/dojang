def paging(m, n):
    pages = 0
    
    if n < 1 or m < n:
        return False

    return m//n if m%n ==0 else m//n + 1


if __name__ == '__main__':
    print(paging(10, 2))  # Answer = 5
    print(paging(10, 3))  # Answer = 4
    print(paging(10, 6))  # Answer = 2
    print(paging(10, 11)) # False