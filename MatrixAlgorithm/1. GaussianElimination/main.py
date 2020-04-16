import numpy as np
from numpy import *


def backward_substitution(upper_triangular_matrix, b):
    dimension = len(upper_triangular_matrix)
    x = np.zeros((dimension, 1))
    for i in range(dimension):
        index = dimension - i - 1
        h = 0
        for j in range(i):
            h += upper_triangular_matrix[index][index + j + 1] * x[index + j + 1]
        x[index][0] = (b[index][0] - h) / upper_triangular_matrix[index][index]
    return x


# similar to backward_substitution
def forward_substitution(lower_triangular_matrix, b):
    dimension = len(lower_triangular_matrix)
    x = np.zeros((dimension, 1))
    for index in range(dimension):
        h = 0
        for j in range(index):
            h += lower_triangular_matrix[index][j] * x[j]
        x[index][0] = b[index][0] - h
    return x


if __name__ == '__main__':

    # example of backword substitution
    upper_triangular_matrix = np.asarray([[2,1,1], [0,1,1], [0,0,2]])
    b_b = np.asarray([[4], [2], [2]])

    print('solving Ax = b ( A is upper triangular matrix)\n')
    print(f'A :\n {upper_triangular_matrix} \n')
    print(f'b:\n {b_b} \n')
    print('solving equation by using backword substitution...\n')
    b_x = backward_substitution(upper_triangular_matrix, b_b)
    print(f'result is :\n {b_x} \n')

    # example of forward substitution
    lower_triangular_matrix = np.asarray([[1, 0, 0], [4, 1, 0], [5, 6, 1]])
    f_b = np.asarray([[2], [4], [6]])

    print('solving Ax = b ( A is lower triangular matrix)\n')
    print(f'A :\n {lower_triangular_matrix} \n')
    print(f'b:\n {f_b} \n')
    print('solving equation by using forward substitution...\n')
    f_x = forward_substitution(lower_triangular_matrix, f_b)
    print(f'result is :\n {f_x} \n')



