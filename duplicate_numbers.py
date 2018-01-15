def duplicate_numbers(s):
    l = s.split()
    for item in l:
        if ''.join(sorted(item)) == '0123456789':
            print('true', end=' ')
        else:
            print('false', end=' ')



if __name__ == '__main__':
    s = '0123456789 01234 01234567890 6789012345 012322456789'
    print(duplicate_numbers(s))

