import numpy as np


def multiply_2_array(array1, array2):
    print("Before multiply")
    print(array1)
    print(array2)
    matrix = np.multiply(array1, array2)
    print("After multiply")
    print(matrix)
    return matrix


if __name__ == '__main__':
    multiply_2_array(np.array([[1, 2], [3, 4]]), np.array([[3, 4], [5, 6]]))
    multiply_2_array(np.array([[1, 2], [3, 4]]), np.array([[3, 4], [5, 6]]))
