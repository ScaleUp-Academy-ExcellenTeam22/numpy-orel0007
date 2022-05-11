import numpy as np


def find_size_matrix(matrix):
    """
    Get matrix and return the size of rows and cols.
    :param matrix:
    :return:(tuple) Size rows and cols of the matrix.
    """
    return np.shape(matrix)


if __name__ == '__main__':
    print(find_size_matrix([[2, 3], [4, 5], [5, 7]]))
    print(find_size_matrix([[2, 3, 5], [4, 5, 6], [5, 7, 8]]))
    print(find_size_matrix([2, 3, 4, 6, 5, 7]))

