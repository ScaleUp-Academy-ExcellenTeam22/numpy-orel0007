import numpy as np


def add_vector_to_row_5(vec, matrix):
    """
    Create new vector after add each row of the matrix by the given vector.
    :param vec:(list) Given vector to add to each row in the matrix.
    :param matrix:(np array) Given matrix.
    :return: New vector: the result of add the given vector to each row.
    """
    result = np.empty_like(matrix)
    for i in range(len(matrix)):
        result[i, :] = matrix[i, :] + vec
    return result


if __name__ == '__main__':
    print(add_vector_to_row_5([1, 2], np.array([[4, 5], [6, 7], [8, 9]])))
