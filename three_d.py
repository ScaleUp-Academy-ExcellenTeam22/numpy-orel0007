import numpy as np


def three_d():
    """
    create a 3-D array with ones on a diagonal and zeros elsewhere
    :return: 3-D array.
    """
    return np.eye(3)


if __name__ == '__main__':
    print(three_d())
