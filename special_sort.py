def special_sort(numbers):
    return [x for x in numbers if x <= 0] + [x for x in numbers if x > 0]

if __name__ == '__main__':
    num_list = [-1, 1, 3, -2, 2]
    print(special_sort(num_list))