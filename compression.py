def compression():
    strings = input('Enter Strings :')
    count = 0
    for i, string in enumerate(strings):
        if strings[i] == strings[i+1]:
            count += 1
        else:
            count += 1

    print(count)


compression()
