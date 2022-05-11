# importing numpy
import numpy as np


def change_sign_vector(np1, range1, range2):
    """
    Get numpy array and change the sign of -/+ of the array in range of the give inputs: range1-rang2.
    :param np1:(np.array)
    :param range1:(int) Start place to change parameters sign.
    :param range2:(int) End place to change parameters sign.
    :return: Numpy array with different sign -/+ in range of range1:range2
    """
    np1[range1:range2+1] *= -1
    return np1


if __name__ == '__main__':
    print(change_sign_vector(np.array(range(21)), 9, 15))

