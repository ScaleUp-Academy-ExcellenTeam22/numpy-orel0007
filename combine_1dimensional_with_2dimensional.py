import numpy as np


def combine_1dimensional_with_2dimensional(arr1, arr2):
    """
    Combine 1d dimensional with 2 dimensional array and display their elements.
    :param arr1: Numpy array1 1D
    :param arr2: Numpy array1 2D
    """
    for a, b in np.nditer([arr1, arr2]):
        print("%d:%d" % (a, b), )


if __name__ == '__main__':

    array1 = np.arange(4)
    array2 = np.arange(8).reshape(2, 4)
    print("1D array:")
    print(array1)
    print("2D array:")
    print(array2)
    combine_1dimensional_with_2dimensional(array1, array2)
