MAX_ROW_NUMBER = 6
MAX_COL_NUMBER = 6


def print_array(matrix):
    for i in range(MAX_ROW_NUMBER):
        for j in range(MAX_COL_NUMBER):
            print('{:>2d}'.format(matrix[i][j]), end=' ')
        print('')


def spiral_array(matrix):
    number = 1
    for i in range(MAX_ROW_NUMBER):
        for j in range(MAX_COL_NUMBER):
            matrix[i][j] = number
            number += 1
    return matrix


if __name__ == '__main__':
    matrix = [[0 for i in range(MAX_COL_NUMBER)] for j in range(MAX_ROW_NUMBER)]
    spiral_array(matrix)
    print_array(matrix)



