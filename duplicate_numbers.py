def duplicate_numbers(s):
    d = {}
    for c in s:
        if c not in dict.keys():
            d[c] = 1
        else:
            d[c] += 1
    
    for value in dict.values():
        if value > 1:
            print('False', end=' ')
        else:
            print('True', end=' ')





if __name__ == '__main__':
    sample = '0123456789 01234'
    sample = sample.replace(' ', '')
    print(duplicate_numbers(sample))


