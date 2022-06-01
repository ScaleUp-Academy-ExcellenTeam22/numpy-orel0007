import numpy as np


def matrix_10_10_insert_1_or_0() -> np.arrange:
    """
    Create vector 10*10 size when the borders equal to 1 and inside 0.
    :return: Vector of borders equal 1, inside 0.
    """
    vec = np.ones((10, 10))
    vec[1:-1, 1:-1] = 0
    return vec


if __name__ == '__main__':
    print(matrix_10_10_insert_1_or_0())
