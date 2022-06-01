import numpy as np


def remove_single_dimensional(arr):
    """
    Remove single-dimensional .
    :param arr: Numpy array.
    :return:New shape of the numoy array after squeeze.
    """
    print(np.squeeze(arr).shape)


if __name__ == '__main__':
    array = np.zeros((3, 1, 4))
    remove_single_dimensional(array)
