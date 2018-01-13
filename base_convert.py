def base_convert(number, base):
    T = '0123456789ABCDE'
    q, r = divmod(number, base)
    if q == 0:
        return T[r]
    else:
        return base_convert(q, base) + T[r]


if __name__ == '__main__':
    print(base_convert(2333, 2))
    print(base_convert(2333, 8))
    print(base_convert(2333, 16))

