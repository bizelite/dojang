def pothole_case(s):
    for c in s:
        if c.isupper() or c.isdigit():
            s = s.replace(c, '_' + c.lower())
    return s



if __name__ == '__main__':
    print(pothole_case('codingDojang'))
    print(pothole_case('numGoat30'))