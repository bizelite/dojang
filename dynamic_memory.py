int_count = int(input('Enter a number of integer: '))

total = 0
average = 0
count = 0

while count < int_count:
    number = int(input('Enter a number: '))
    total += number
    count += 1

average = total / int_count
print('Total = {}, Average = {}'.format(total, average))

del total, average, count


