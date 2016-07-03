def printing_ox():
    number = int(input('Enter a number: '))
    for num in range(1, number+1):
        print('O' * (number - num) + 'X' * num)

printing_ox()
