import numpy as np


def random_values_swap_rows(limit):
    """
    Create matrix 4*4 with random values from 0-limit, than swap the first row with the last row.
    :param limit: The limit of the random values.
    :return: Matrix 4*4.
    """
    vector = np.random.randint(limit, size=(4, 4))
    print("Before swap first and end row: ")
    print(vector)
    vector[[0, -1]] = vector[[-1, 0]]
    print("After swap first and end row: ")
    print(vector)
    return vector


if __name__ == '__main__':
    random_values_swap_rows(50)
